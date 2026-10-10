/* ==========================================================================
   FREC Master Pro - Application Logic & State Engine
   ========================================================================== */

(function () {
  'use strict';

  // --- AUDIO SYNTHESIZER (Web Audio API) ---
  const soundSystem = {
    audioCtx: null,
    enabled: true,

    init() {
      if (!this.audioCtx && (window.AudioContext || window.webkitAudioContext)) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        this.audioCtx = new AudioCtx();
      }
    },

    playTone(freq, type = 'sine', duration = 0.15, gainVal = 0.08) {
      if (!this.enabled) return;
      try {
        this.init();
        if (this.audioCtx && this.audioCtx.state === 'suspended') {
          this.audioCtx.resume();
        }
        if (!this.audioCtx) return;

        const osc = this.audioCtx.createOscillator();
        const gain = this.audioCtx.createGain();

        osc.type = type;
        osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);

        gain.gain.setValueAtTime(gainVal, this.audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, this.audioCtx.currentTime + duration);

        osc.connect(gain);
        gain.connect(this.audioCtx.destination);

        osc.start();
        osc.stop(this.audioCtx.currentTime + duration);
      } catch (e) {
        // Audio might be blocked until user interacts
      }
    },

    playSuccess() {
      this.playTone(523.25, 'sine', 0.1, 0.06); // C5
      setTimeout(() => this.playTone(659.25, 'sine', 0.12, 0.07), 80); // E5
      setTimeout(() => this.playTone(783.99, 'sine', 0.25, 0.08), 160); // G5
    },

    playError() {
      this.playTone(280, 'triangle', 0.15, 0.07);
      setTimeout(() => this.playTone(220, 'triangle', 0.25, 0.07), 100);
    },

    playClick() {
      this.playTone(400, 'sine', 0.04, 0.03);
    },

    toggleSound() {
      this.enabled = !this.enabled;
      localStorage.setItem('frec_sound', this.enabled ? '1' : '0');
      return this.enabled;
    }
  };

  // --- LOCAL STORAGE DATA PERSISTENCE ---
  const storage = {
    getFavorites() {
      try {
        return new Set(JSON.parse(localStorage.getItem('frec_favorites') || '[]'));
      } catch (e) {
        return new Set();
      }
    },
    saveFavorites(favSet) {
      localStorage.setItem('frec_favorites', JSON.stringify(Array.from(favSet)));
    },
    getExamStats() {
      try {
        return JSON.parse(localStorage.getItem('frec_exam_stats') || '{"examsTaken": 0, "bestScore": 0, "avgScore": 0}');
      } catch (e) {
        return { examsTaken: 0, bestScore: 0, avgScore: 0 };
      }
    },
    saveExamResult(scorePercent) {
      const stats = this.getExamStats();
      stats.examsTaken += 1;
      if (scorePercent > stats.bestScore) stats.bestScore = scorePercent;
      stats.avgScore = Math.round(((stats.avgScore * (stats.examsTaken - 1)) + scorePercent) / stats.examsTaken);
      localStorage.setItem('frec_exam_stats', JSON.stringify(stats));
    }
  };

  // --- GLOBAL APPLICATION STATE ---
  const state = {
    theme: localStorage.getItem('frec_theme') || 'dark',
    favorites: storage.getFavorites(),
    allQuestions: [],
    categories: [],

    // Active Tab
    currentTab: 'exam',

    // Exam Mode State
    exam: {
      active: false,
      questions: [],
      currentIndex: 0,
      userAnswers: {}, // { [index]: selectedOptionIndex }
      shuffledOptions: {}, // { [index]: { options: [], correctIndex: number } }
      flagged: new Set(),
      timer: null,
      timeRemaining: 0,
      totalTime: 0,
      isReviewMode: false,
      reviewFilter: 'all' // 'all', 'incorrect', 'flagged'
    },

    // Practice Mode State
    practice: {
      questions: [],
      currentIndex: 0,
      shuffledOptions: {},
      selectedOption: null,
      hasSubmitted: false,
      categoryFilter: 'all'
    },

    // Flashcards State
    flashcards: {
      questions: [],
      currentIndex: 0,
      isFlipped: false,
      categoryFilter: 'all',
      mastered: new Set()
    },

    // Guide State
    guide: {
      searchQuery: '',
      categoryFilter: 'all',
      hideAnswers: false
    }
  };

  // --- HELPER FUNCTIONS ---
  function shuffle(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function formatTime(seconds) {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    if (hrs > 0) {
      return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  // --- INITIALIZATION ---
  function initApp() {
    // 1. Load questions from window.QUESTIONS_DATA
    if (typeof QUESTIONS_DATA !== 'undefined' && Array.isArray(QUESTIONS_DATA)) {
      state.allQuestions = QUESTIONS_DATA;
    } else {
      console.error('No se pudo encontrar QUESTIONS_DATA');
      return;
    }

    // 2. Extract unique categories
    const catSet = new Set();
    state.allQuestions.forEach(q => catSet.add(q.category));
    state.categories = Array.from(catSet);

    // 3. Set initial theme
    document.documentElement.setAttribute('data-theme', state.theme);
    updateThemeToggleBtn();

    // 4. Set initial audio state
    soundSystem.enabled = localStorage.getItem('frec_sound') !== '0';
    updateSoundToggleBtn();

    // 5. Populate Category Dropdowns
    populateCategorySelectors();

    // 6. Setup DOM Event Listeners
    setupEventListeners();

    // 7. Update Header Stats
    updateHeaderStats();

    // 8. Render Guide initially
    filterAndRenderGuide();

    // 9. Init flashcards
    initFlashcards();
  }

  function updateThemeToggleBtn() {
    const btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;
    btn.innerHTML = state.theme === 'light' ? '🌙' : '☀️';
    btn.title = state.theme === 'light' ? 'Cambiar a Modo Oscuro' : 'Cambiar a Modo Claro';
  }

  function updateSoundToggleBtn() {
    const btn = document.getElementById('sound-toggle-btn');
    if (!btn) return;
    btn.innerHTML = soundSystem.enabled ? '🔊' : '🔇';
    btn.title = soundSystem.enabled ? 'Silenciar Efectos de Sonido' : 'Activar Sonidos';
  }

  function populateCategorySelectors() {
    const selectors = ['exam-category-select', 'practice-category-select', 'flashcards-category-select', 'guide-category-select'];
    selectors.forEach(id => {
      const el = document.getElementById(id);
      if (!el) return;
      el.innerHTML = '<option value="all">Todas las Categorías (200 Preguntas)</option>';
      state.categories.forEach(cat => {
        const count = state.allQuestions.filter(q => q.category === cat).length;
        const opt = document.createElement('option');
        opt.value = cat;
        opt.textContent = `${cat} (${count} preguntas)`;
        el.appendChild(opt);
      });
    });
  }

  function updateHeaderStats() {
    const stats = storage.getExamStats();
    const statEl = document.getElementById('header-best-score');
    if (statEl) {
      statEl.textContent = `${stats.bestScore}%`;
    }
    const favCountEl = document.getElementById('header-fav-count');
    if (favCountEl) {
      favCountEl.textContent = state.favorites.size;
    }
  }

  // --- EVENT LISTENERS ---
  function setupEventListeners() {
    // Mode Navigation Tabs
    document.querySelectorAll('.nav-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetTab = btn.getAttribute('data-tab');
        switchTab(targetTab);
        soundSystem.playClick();
      });
    });

    // Theme Toggle
    document.getElementById('theme-toggle-btn').addEventListener('click', () => {
      state.theme = state.theme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', state.theme);
      localStorage.setItem('frec_theme', state.theme);
      updateThemeToggleBtn();
      soundSystem.playClick();
    });

    // Sound Toggle
    document.getElementById('sound-toggle-btn').addEventListener('click', () => {
      const enabled = soundSystem.toggleSound();
      updateSoundToggleBtn();
      if (enabled) soundSystem.playTone(500, 'sine', 0.1);
    });

    // --- EXAM MODE CONTROLS ---
    // Start Exam Button
    document.getElementById('start-exam-btn').addEventListener('click', () => {
      startExam();
    });

    // Previous Question
    document.getElementById('exam-prev-btn').addEventListener('click', () => {
      if (state.exam.currentIndex > 0) {
        state.exam.currentIndex--;
        renderExamQuestion();
        soundSystem.playClick();
      }
    });

    // Next Question
    document.getElementById('exam-next-btn').addEventListener('click', () => {
      if (state.exam.currentIndex < state.exam.questions.length - 1) {
        state.exam.currentIndex++;
        renderExamQuestion();
        soundSystem.playClick();
      }
    });

    // Flag Question
    document.getElementById('exam-flag-btn').addEventListener('click', () => {
      const curQ = state.exam.questions[state.exam.currentIndex];
      if (state.exam.flagged.has(curQ.id)) {
        state.exam.flagged.delete(curQ.id);
      } else {
        state.exam.flagged.add(curQ.id);
      }
      renderExamQuestion();
      renderExamPalette();
      soundSystem.playClick();
    });

    // Bookmark / Favorite Question in Exam
    document.getElementById('exam-fav-btn').addEventListener('click', () => {
      const curQ = state.exam.questions[state.exam.currentIndex];
      toggleFavorite(curQ.id);
      renderExamQuestion();
    });

    // Finish Exam Button (prompts modal)
    document.getElementById('exam-finish-btn').addEventListener('click', () => {
      promptFinishExam();
    });

    // Modal Actions
    document.getElementById('modal-cancel-btn').addEventListener('click', () => {
      closeModal();
    });
    document.getElementById('modal-confirm-btn').addEventListener('click', () => {
      closeModal();
      finishExam();
    });

    // Results Actions
    document.getElementById('results-retry-btn').addEventListener('click', () => {
      document.getElementById('exam-results-screen').style.display = 'none';
      document.getElementById('exam-setup-screen').style.display = 'block';
    });

    document.getElementById('results-review-btn').addEventListener('click', () => {
      startReviewMode();
    });

    // --- PRACTICE MODE CONTROLS ---
    document.getElementById('practice-category-select').addEventListener('change', (e) => {
      state.practice.categoryFilter = e.target.value;
      initPracticeMode();
    });

    document.getElementById('practice-prev-btn').addEventListener('click', () => {
      if (state.practice.currentIndex > 0) {
        state.practice.currentIndex--;
        state.practice.hasSubmitted = false;
        state.practice.selectedOption = null;
        renderPracticeQuestion();
        soundSystem.playClick();
      }
    });

    document.getElementById('practice-next-btn').addEventListener('click', () => {
      if (state.practice.currentIndex < state.practice.questions.length - 1) {
        state.practice.currentIndex++;
        state.practice.hasSubmitted = false;
        state.practice.selectedOption = null;
        renderPracticeQuestion();
        soundSystem.playClick();
      }
    });

    document.getElementById('practice-fav-btn').addEventListener('click', () => {
      const curQ = state.practice.questions[state.practice.currentIndex];
      toggleFavorite(curQ.id);
      renderPracticeQuestion();
    });

    // --- FLASHCARD CONTROLS ---
    const flashcardCard = document.getElementById('flashcard-card');
    flashcardCard.addEventListener('click', () => {
      state.flashcards.isFlipped = !state.flashcards.isFlipped;
      flashcardCard.classList.toggle('flipped', state.flashcards.isFlipped);
      soundSystem.playClick();
    });

    document.getElementById('flashcard-prev-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      if (state.flashcards.currentIndex > 0) {
        state.flashcards.currentIndex--;
        state.flashcards.isFlipped = false;
        renderFlashcard();
        soundSystem.playClick();
      }
    });

    document.getElementById('flashcard-next-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      if (state.flashcards.currentIndex < state.flashcards.questions.length - 1) {
        state.flashcards.currentIndex++;
        state.flashcards.isFlipped = false;
        renderFlashcard();
        soundSystem.playClick();
      }
    });

    document.getElementById('flashcard-flip-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      state.flashcards.isFlipped = !state.flashcards.isFlipped;
      flashcardCard.classList.toggle('flipped', state.flashcards.isFlipped);
      soundSystem.playClick();
    });

    document.getElementById('flashcard-fav-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      const curQ = state.flashcards.questions[state.flashcards.currentIndex];
      toggleFavorite(curQ.id);
      renderFlashcard();
    });

    document.getElementById('flashcards-category-select').addEventListener('change', (e) => {
      state.flashcards.categoryFilter = e.target.value;
      initFlashcards();
    });

    // --- GUIDE SEARCH & FILTERS ---
    const searchInput = document.getElementById('guide-search-input');
    searchInput.addEventListener('input', (e) => {
      state.guide.searchQuery = e.target.value.toLowerCase().trim();
      filterAndRenderGuide();
    });

    document.getElementById('guide-category-select').addEventListener('change', (e) => {
      state.guide.categoryFilter = e.target.value;
      filterAndRenderGuide();
    });

    document.getElementById('guide-toggle-answers-btn').addEventListener('click', () => {
      state.guide.hideAnswers = !state.guide.hideAnswers;
      const btn = document.getElementById('guide-toggle-answers-btn');
      btn.textContent = state.guide.hideAnswers ? '👁️ Mostrar Respuestas' : '🙈 Ocultar Respuestas para Autoevaluación';
      filterAndRenderGuide();
      soundSystem.playClick();
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      // Don't trigger shortcuts if inside search input
      if (document.activeElement === searchInput) return;

      if (state.currentTab === 'exam' && state.exam.active && !state.exam.isReviewMode) {
        if (['1', '2', '3', '4'].includes(e.key)) {
          const optIdx = parseInt(e.key, 10) - 1;
          selectExamOption(optIdx);
        } else if (e.key.toLowerCase() === 'a') selectExamOption(0);
        else if (e.key.toLowerCase() === 'b') selectExamOption(1);
        else if (e.key.toLowerCase() === 'c') selectExamOption(2);
        else if (e.key.toLowerCase() === 'd') selectExamOption(3);
        else if (e.key === 'ArrowRight') document.getElementById('exam-next-btn').click();
        else if (e.key === 'ArrowLeft') document.getElementById('exam-prev-btn').click();
        else if (e.key.toLowerCase() === 'f') document.getElementById('exam-flag-btn').click();
      } else if (state.currentTab === 'practice') {
        if (['1', '2', '3', '4'].includes(e.key)) {
          selectPracticeOption(parseInt(e.key, 10) - 1);
        } else if (e.key.toLowerCase() === 'a') selectPracticeOption(0);
        else if (e.key.toLowerCase() === 'b') selectPracticeOption(1);
        else if (e.key.toLowerCase() === 'c') selectPracticeOption(2);
        else if (e.key.toLowerCase() === 'd') selectPracticeOption(3);
        else if (e.key === 'ArrowRight') document.getElementById('practice-next-btn').click();
        else if (e.key === 'ArrowLeft') document.getElementById('practice-prev-btn').click();
      } else if (state.currentTab === 'flashcards') {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          document.getElementById('flashcard-flip-btn').click();
        } else if (e.key === 'ArrowRight') document.getElementById('flashcard-next-btn').click();
        else if (e.key === 'ArrowLeft') document.getElementById('flashcard-prev-btn').click();
      }
    });
  }

  function toggleFavorite(id) {
    if (state.favorites.has(id)) {
      state.favorites.delete(id);
    } else {
      state.favorites.add(id);
    }
    storage.saveFavorites(state.favorites);
    updateHeaderStats();
    soundSystem.playClick();
  }

  // --- TAB SWITCHING ---
  function switchTab(tabName) {
    state.currentTab = tabName;
    document.querySelectorAll('.nav-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabName);
    });

    document.querySelectorAll('.tab-view').forEach(view => {
      view.classList.remove('active');
    });

    const activeView = document.getElementById(`view-${tabName}`);
    if (activeView) activeView.classList.add('active');

    // Trigger tab specific setups
    if (tabName === 'practice') {
      initPracticeMode();
    } else if (tabName === 'flashcards') {
      initFlashcards();
    } else if (tabName === 'guide') {
      filterAndRenderGuide();
    }
  }

  // --- EXAM MODE LOGIC ---
  function startExam() {
    const qCountSetting = document.querySelector('input[name="exam-count"]:checked').value;
    const timeLimitSetting = document.getElementById('exam-time-limit').value;
    const categorySetting = document.getElementById('exam-category-select').value;

    let pool = [...state.allQuestions];
    if (categorySetting !== 'all') {
      pool = pool.filter(q => q.category === categorySetting);
    }

    if (qCountSetting === 'favs') {
      pool = pool.filter(q => state.favorites.has(q.id));
      if (pool.length === 0) {
        alert('No tienes preguntas marcadas como favoritas todavía. ¡Agrega preguntas con la estrella ⭐ para practicar esta selección!');
        return;
      }
    }

    // Shuffle question pool
    pool = shuffle(pool);

    // Limit count
    let count = pool.length;
    if (qCountSetting === '50') count = Math.min(50, pool.length);
    else if (qCountSetting === '100') count = Math.min(100, pool.length);
    else if (qCountSetting === '200') count = Math.min(200, pool.length);

    state.exam.questions = pool.slice(0, count);
    state.exam.currentIndex = 0;
    state.exam.userAnswers = {};
    state.exam.shuffledOptions = {};
    state.exam.flagged = new Set();
    state.exam.active = true;
    state.exam.isReviewMode = false;

    // Generate randomized options for each question
    state.exam.questions.forEach((q, idx) => {
      const allOpts = [q.answer, ...q.distractors];
      const shuffled = shuffle(allOpts);
      state.exam.shuffledOptions[idx] = {
        options: shuffled,
        correctIndex: shuffled.indexOf(q.answer)
      };
    });

    // Setup Timer
    if (state.exam.timer) clearInterval(state.exam.timer);
    const minutes = parseInt(timeLimitSetting, 10);
    if (minutes > 0) {
      state.exam.totalTime = minutes * 60;
      state.exam.timeRemaining = state.exam.totalTime;
      startExamTimer();
    } else {
      state.exam.totalTime = 0;
      state.exam.timeRemaining = 0;
      document.getElementById('exam-timer-display').textContent = '⏱️ Ilimitado';
      document.getElementById('exam-timer-display').classList.remove('urgent');
    }

    // UI Switches
    document.getElementById('exam-setup-screen').style.display = 'none';
    document.getElementById('exam-results-screen').style.display = 'none';
    document.getElementById('exam-active-screen').style.display = 'block';

    renderExamQuestion();
    renderExamPalette();
    soundSystem.playClick();
  }

  function startExamTimer() {
    const timerDisplay = document.getElementById('exam-timer-display');
    timerDisplay.classList.remove('urgent');

    state.exam.timer = setInterval(() => {
      state.exam.timeRemaining--;

      if (state.exam.timeRemaining <= 300) {
        timerDisplay.classList.add('urgent');
      }

      timerDisplay.textContent = `⏱️ ${formatTime(state.exam.timeRemaining)}`;

      if (state.exam.timeRemaining <= 0) {
        clearInterval(state.exam.timer);
        alert('¡El tiempo oficial del examen ha concluido!');
        finishExam();
      }
    }, 1000);
  }

  function renderExamQuestion() {
    const qIndex = state.exam.currentIndex;
    const question = state.exam.questions[qIndex];
    const totalQ = state.exam.questions.length;

    // Header info
    document.getElementById('exam-question-category').textContent = question.category;
    document.getElementById('exam-q-number-indicator').textContent = `Pregunta ${qIndex + 1} de ${totalQ}`;
    
    // Progress bar
    const progressPercent = ((qIndex + 1) / totalQ) * 100;
    document.getElementById('exam-progress-bar-fill').style.width = `${progressPercent}%`;

    // Flag button state
    const flagBtn = document.getElementById('exam-flag-btn');
    const isFlagged = state.exam.flagged.has(question.id);
    flagBtn.classList.toggle('flagged', isFlagged);
    flagBtn.innerHTML = isFlagged ? '🚩 Marcada' : '🏳️ Marcar';

    // Favorite button state
    const favBtn = document.getElementById('exam-fav-btn');
    const isFav = state.favorites.has(question.id);
    favBtn.classList.toggle('favorited', isFav);
    favBtn.innerHTML = isFav ? '⭐ En Favoritos' : '☆ Guardar';

    // Question Text
    document.getElementById('exam-question-text').textContent = question.question;

    // Render Options
    const optionsList = document.getElementById('exam-options-list');
    optionsList.innerHTML = '';

    const { options, correctIndex } = state.exam.shuffledOptions[qIndex];
    const selectedOption = state.exam.userAnswers[qIndex];
    const letters = ['A', 'B', 'C', 'D'];

    options.forEach((optText, optIdx) => {
      const optItem = document.createElement('div');
      optItem.className = 'option-item';
      if (selectedOption === optIdx) optItem.classList.add('selected');

      // If in review mode, show correct/incorrect markers
      if (state.exam.isReviewMode) {
        if (optIdx === correctIndex) {
          optItem.classList.add('correct');
        } else if (selectedOption === optIdx && selectedOption !== correctIndex) {
          optItem.classList.add('incorrect');
        }
      }

      optItem.innerHTML = `
        <div class="option-letter">${letters[optIdx]}</div>
        <div class="option-content">${optText}</div>
      `;

      if (!state.exam.isReviewMode) {
        optItem.addEventListener('click', () => {
          selectExamOption(optIdx);
        });
      }

      optionsList.appendChild(optItem);
    });

    // Review mode explanation box
    const feedbackBox = document.getElementById('exam-review-feedback');
    if (state.exam.isReviewMode) {
      feedbackBox.style.display = 'block';
      const isCorrect = selectedOption === correctIndex;
      feedbackBox.className = `feedback-box show ${isCorrect ? 'correct' : 'incorrect'}`;
      feedbackBox.innerHTML = `
        <div class="feedback-title">${isCorrect ? '✓ Respuesta Correcta' : '✗ Respuesta Incorrecta'}</div>
        <div class="feedback-text"><strong>Respuesta oficial de la guía:</strong> ${question.answer}</div>
        <div class="feedback-text" style="margin-top: 0.5rem; color: var(--text-secondary);">${question.explanation}</div>
      `;
    } else {
      feedbackBox.style.display = 'none';
    }

    // Navigation buttons state
    document.getElementById('exam-prev-btn').disabled = qIndex === 0;
    const nextBtn = document.getElementById('exam-next-btn');
    if (qIndex === totalQ - 1) {
      nextBtn.textContent = state.exam.isReviewMode ? 'Volver a Resultados 📊' : 'Revisar / Finalizar 🏁';
    } else {
      nextBtn.textContent = 'Siguiente ❯';
    }

    renderExamPalette();
  }

  function selectExamOption(optIdx) {
    state.exam.userAnswers[state.exam.currentIndex] = optIdx;
    soundSystem.playClick();
    renderExamQuestion();
    renderExamPalette();
  }

  function renderExamPalette() {
    const grid = document.getElementById('exam-palette-grid');
    if (!grid) return;
    grid.innerHTML = '';

    state.exam.questions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = idx + 1;

      if (idx === state.exam.currentIndex) btn.classList.add('current');
      if (state.exam.userAnswers[idx] !== undefined) btn.classList.add('answered');
      if (state.exam.flagged.has(q.id)) btn.classList.add('flagged');

      btn.addEventListener('click', () => {
        state.exam.currentIndex = idx;
        renderExamQuestion();
        soundSystem.playClick();
      });

      grid.appendChild(btn);
    });
  }

  function promptFinishExam() {
    const totalQ = state.exam.questions.length;
    const answeredCount = Object.keys(state.exam.userAnswers).length;
    const flaggedCount = state.exam.flagged.size;
    const unanswered = totalQ - answeredCount;

    let message = `Has respondido <strong>${answeredCount} de ${totalQ}</strong> preguntas.`;
    if (unanswered > 0) {
      message += `<br><span style="color: var(--warning);">⚠️ Tienes ${unanswered} preguntas sin responder.</span>`;
    }
    if (flaggedCount > 0) {
      message += `<br>Tienes <strong>${flaggedCount}</strong> preguntas marcadas para revisión.`;
    }
    message += `<br><br>¿Estás seguro de que deseas entregar el examen ahora?`;

    document.getElementById('modal-title').textContent = 'Confirmar Entrega de Examen';
    document.getElementById('modal-body').innerHTML = message;
    document.getElementById('modal-overlay').classList.add('active');
  }

  function closeModal() {
    document.getElementById('modal-overlay').classList.remove('active');
  }

  function finishExam() {
    if (state.exam.timer) clearInterval(state.exam.timer);
    state.exam.active = false;

    // Calculate Scores
    let correctCount = 0;
    const categoryBreakdown = {};

    state.exam.questions.forEach((q, idx) => {
      const selected = state.exam.userAnswers[idx];
      const correctIdx = state.exam.shuffledOptions[idx].correctIndex;
      const isCorrect = selected === correctIdx;

      if (isCorrect) correctCount++;

      if (!categoryBreakdown[q.category]) {
        categoryBreakdown[q.category] = { total: 0, correct: 0 };
      }
      categoryBreakdown[q.category].total++;
      if (isCorrect) categoryBreakdown[q.category].correct++;
    });

    const totalQ = state.exam.questions.length;
    const scorePercent = Math.round((correctCount / totalQ) * 100);
    const passed = scorePercent >= 75; // Florida FREC requirement is 75%

    // Save result to storage
    storage.saveExamResult(scorePercent);
    updateHeaderStats();

    // Render Results View
    document.getElementById('exam-active-screen').style.display = 'none';
    const resultsScreen = document.getElementById('exam-results-screen');
    resultsScreen.style.display = 'block';

    const scoreBadge = document.getElementById('results-score-badge');
    scoreBadge.className = `score-badge-large ${passed ? 'passed' : 'failed'}`;
    document.getElementById('results-score-percent').textContent = `${scorePercent}%`;
    document.getElementById('results-score-fraction').textContent = `${correctCount}/${totalQ}`;

    const verdictEl = document.getElementById('results-verdict');
    verdictEl.className = `results-verdict ${passed ? 'passed' : 'failed'}`;
    verdictEl.textContent = passed ? '¡APROBADO! 🎉' : 'NO APROBADO (Requiere Refuerzo)';

    const summaryText = document.getElementById('results-summary-text');
    if (passed) {
      summaryText.textContent = `¡Felicitaciones! Has superado el umbral oficial del 75% requerido por la Comisión de Bienes Raíces de la Florida (FREC). Tu preparación está en excelente nivel.`;
      soundSystem.playSuccess();
      launchConfetti();
    } else {
      summaryText.textContent = `Has obtenido un ${scorePercent}%. El examen oficial de Florida exige un mínimo de 75% (75/100) para aprobar. Revisa el desglose de categorías abajo para reforzar los temas donde tuviste errores.`;
      soundSystem.playError();
    }

    document.getElementById('result-stat-correct').textContent = correctCount;
    document.getElementById('result-stat-incorrect').textContent = totalQ - correctCount;
    document.getElementById('result-stat-time').textContent = state.exam.totalTime > 0 
      ? formatTime(state.exam.totalTime - state.exam.timeRemaining) 
      : 'Modo Libre';

    // Category Breakdown Render
    const categoryContainer = document.getElementById('results-category-breakdown');
    categoryContainer.innerHTML = '<h4>Desglose de Desempeño por Categoría</h4>';

    for (const [cat, data] of Object.entries(categoryBreakdown)) {
      const catPercent = Math.round((data.correct / data.total) * 100);
      const row = document.createElement('div');
      row.className = 'category-stat-row';
      row.innerHTML = `
        <span style="width: 180px; font-weight: 600;">${cat}</span>
        <div class="category-stat-bar-bg">
          <div class="category-stat-bar-fill" style="width: ${catPercent}%; background-color: ${catPercent >= 75 ? 'var(--success)' : 'var(--danger)'};"></div>
        </div>
        <span style="width: 80px; text-align: right; font-weight: 700;">${data.correct}/${data.total} (${catPercent}%)</span>
      `;
      categoryContainer.appendChild(row);
    }
  }

  function startReviewMode() {
    state.exam.isReviewMode = true;
    state.exam.currentIndex = 0;
    document.getElementById('exam-results-screen').style.display = 'none';
    document.getElementById('exam-active-screen').style.display = 'block';
    renderExamQuestion();
  }

  // --- PRACTICE MODE LOGIC ---
  function initPracticeMode() {
    let pool = [...state.allQuestions];
    if (state.practice.categoryFilter !== 'all') {
      pool = pool.filter(q => q.category === state.practice.categoryFilter);
    }

    state.practice.questions = pool;
    state.practice.currentIndex = 0;
    state.practice.hasSubmitted = false;
    state.practice.selectedOption = null;

    // Generate shuffled options
    state.practice.shuffledOptions = {};
    state.practice.questions.forEach((q, idx) => {
      const allOpts = [q.answer, ...q.distractors];
      const shuffled = shuffle(allOpts);
      state.practice.shuffledOptions[idx] = {
        options: shuffled,
        correctIndex: shuffled.indexOf(q.answer)
      };
    });

    renderPracticeQuestion();
  }

  function renderPracticeQuestion() {
    const qIndex = state.practice.currentIndex;
    const question = state.practice.questions[qIndex];
    const totalQ = state.practice.questions.length;

    if (!question) return;

    // Header Info
    document.getElementById('practice-question-category').textContent = question.category;
    document.getElementById('practice-q-number-indicator').textContent = `Pregunta ${qIndex + 1} de ${totalQ}`;

    // Favorite state
    const favBtn = document.getElementById('practice-fav-btn');
    const isFav = state.favorites.has(question.id);
    favBtn.classList.toggle('favorited', isFav);
    favBtn.innerHTML = isFav ? '⭐ En Favoritos' : '☆ Guardar';

    // Question Text
    document.getElementById('practice-question-text').textContent = question.question;

    // Options
    const optionsList = document.getElementById('practice-options-list');
    optionsList.innerHTML = '';

    const { options, correctIndex } = state.practice.shuffledOptions[qIndex];
    const letters = ['A', 'B', 'C', 'D'];

    options.forEach((optText, optIdx) => {
      const optItem = document.createElement('div');
      optItem.className = 'option-item';

      if (state.practice.hasSubmitted) {
        if (optIdx === correctIndex) {
          optItem.classList.add('correct');
        } else if (optIdx === state.practice.selectedOption) {
          optItem.classList.add('incorrect');
        }
      }

      optItem.innerHTML = `
        <div class="option-letter">${letters[optIdx]}</div>
        <div class="option-content">${optText}</div>
      `;

      if (!state.practice.hasSubmitted) {
        optItem.addEventListener('click', () => {
          selectPracticeOption(optIdx);
        });
      }

      optionsList.appendChild(optItem);
    });

    // Feedback
    const feedbackBox = document.getElementById('practice-feedback-box');
    if (state.practice.hasSubmitted) {
      feedbackBox.classList.add('show');
      const isCorrect = state.practice.selectedOption === correctIndex;
      feedbackBox.className = `feedback-box show ${isCorrect ? 'correct' : 'incorrect'}`;
      feedbackBox.innerHTML = `
        <div class="feedback-title">${isCorrect ? '✓ ¡Excelente! Respuesta Correcta' : '✗ Respuesta Incorrecta'}</div>
        <div class="feedback-text"><strong>Respuesta oficial FREC:</strong> ${question.answer}</div>
        <div class="feedback-text" style="margin-top: 0.5rem; color: var(--text-secondary);">${question.explanation}</div>
      `;
    } else {
      feedbackBox.classList.remove('show');
    }

    // Navigation Buttons
    document.getElementById('practice-prev-btn').disabled = qIndex === 0;
    document.getElementById('practice-next-btn').disabled = qIndex === totalQ - 1;
  }

  function selectPracticeOption(optIdx) {
    if (state.practice.hasSubmitted) return;
    state.practice.selectedOption = optIdx;
    state.practice.hasSubmitted = true;

    const { correctIndex } = state.practice.shuffledOptions[state.practice.currentIndex];
    if (optIdx === correctIndex) {
      soundSystem.playSuccess();
    } else {
      soundSystem.playError();
    }

    renderPracticeQuestion();
  }

  // --- FLASHCARDS LOGIC ---
  function initFlashcards() {
    let pool = [...state.allQuestions];
    if (state.flashcards.categoryFilter !== 'all') {
      pool = pool.filter(q => q.category === state.flashcards.categoryFilter);
    }
    state.flashcards.questions = pool;
    state.flashcards.currentIndex = 0;
    state.flashcards.isFlipped = false;
    renderFlashcard();
  }

  function renderFlashcard() {
    const qIndex = state.flashcards.currentIndex;
    const question = state.flashcards.questions[qIndex];
    const totalQ = state.flashcards.questions.length;

    if (!question) return;

    const cardEl = document.getElementById('flashcard-card');
    cardEl.classList.toggle('flipped', state.flashcards.isFlipped);

    document.getElementById('flashcard-counter').textContent = `Tarjeta ${qIndex + 1} de ${totalQ}`;
    document.getElementById('flashcard-category-tag').textContent = question.category;

    // Favorite state
    const favBtn = document.getElementById('flashcard-fav-btn');
    const isFav = state.favorites.has(question.id);
    favBtn.innerHTML = isFav ? '⭐' : '☆';
    favBtn.title = isFav ? 'Quitar de Favoritos' : 'Guardar en Favoritos';

    // Front Question
    document.getElementById('flashcard-front-text').textContent = question.question;

    // Back Answer & Explanation
    document.getElementById('flashcard-back-text').textContent = question.answer;
    document.getElementById('flashcard-explanation-text').textContent = question.explanation;

    // Navigation
    document.getElementById('flashcard-prev-btn').disabled = qIndex === 0;
    document.getElementById('flashcard-next-btn').disabled = qIndex === totalQ - 1;
  }

  // --- MEMORIZATION GUIDE & SEARCH ---
  function filterAndRenderGuide() {
    const query = state.guide.searchQuery;
    const cat = state.guide.categoryFilter;

    let filtered = state.allQuestions.filter(q => {
      const matchCat = cat === 'all' || q.category === cat;
      const matchText = !query || 
        q.question.toLowerCase().includes(query) || 
        q.answer.toLowerCase().includes(query) || 
        q.explanation.toLowerCase().includes(query) ||
        q.id.toString() === query;
      return matchCat && matchText;
    });

    const countIndicator = document.getElementById('guide-count-indicator');
    countIndicator.textContent = `Mostrando ${filtered.length} de ${state.allQuestions.length} preguntas`;

    const container = document.getElementById('guide-items-container');
    container.innerHTML = '';

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 3rem; color: var(--text-secondary);">
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
          <h3>No se encontraron preguntas que coincidan</h3>
          <p>Prueba con otros términos de búsqueda como "escrow", "PITT", "homestead", "título", etc.</p>
        </div>
      `;
      return;
    }

    filtered.forEach(q => {
      const card = document.createElement('div');
      card.className = 'guide-item-card';

      const isFav = state.favorites.has(q.id);

      card.innerHTML = `
        <div class="guide-card-top">
          <span class="category-tag">${q.category}</span>
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span class="guide-card-num">#${q.id}</span>
            <button class="icon-btn" style="width: 28px; height: 28px; font-size: 0.8rem;" title="Marcar favorito" data-fav-id="${q.id}">
              ${isFav ? '⭐' : '☆'}
            </button>
          </div>
        </div>
        <div class="guide-card-q">${q.question}</div>
        <div class="guide-card-a" style="${state.guide.hideAnswers ? 'display: none;' : ''}">
          <span>✓</span>
          <div>${q.answer}</div>
        </div>
        <div class="guide-card-note" style="${state.guide.hideAnswers ? 'display: none;' : ''}">
          💡 <strong>Nota FREC:</strong> ${q.explanation}
        </div>
      `;

      card.querySelector('[data-fav-id]').addEventListener('click', (e) => {
        e.stopPropagation();
        toggleFavorite(q.id);
        filterAndRenderGuide();
      });

      container.appendChild(card);
    });
  }

  // --- SIMPLE CANVASS CONFETTI ---
  function launchConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const pieces = [];
    const colors = ['#2563eb', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#38bdf8'];

    for (let i = 0; i < 120; i++) {
      pieces.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height - canvas.height,
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        velY: Math.random() * 3 + 2,
        velX: (Math.random() - 0.5) * 3,
        rotation: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 8
      });
    }

    let frames = 0;
    function update() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      pieces.forEach(p => {
        p.y += p.velY;
        p.x += p.velX;
        p.rotation += p.rotSpeed;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      });

      frames++;
      if (frames < 200) {
        requestAnimationFrame(update);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    update();
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
