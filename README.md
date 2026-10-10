# 🏛️ FREC Master Pro — Simulador de Examen de Bienes Raíces (Florida)

Simulador interactivo completo para la preparación del examen oficial de **Sales Associate de Florida (FREC / Pearson VUE)**, con el banco completo de **200 preguntas y respuestas oficiales**.

---

## 🚀 Cómo Usar el Simulador

### Opción 1: Abrir directamente en tu navegador (Recomendado)
Simplemente haz doble clic en el archivo [`index.html`](file:///Users/test/Desktop/simulador%20reforzado/index.html) o ábrelo con cualquier navegador web (Chrome, Safari, Edge, Firefox). ¡Funciona 100% sin necesidad de conexión o dependencias externas!

### Opción 2: Usar el servidor local
Si prefieres tenerlo activo con servidor local:
```bash
# Ya se encuentra activo en http://localhost:8123
python3 -m http.server 8123
```
Y abre en tu navegador: [http://localhost:8123](http://localhost:8123)

---

## 📚 Modos de Estudio Incluidos

1. **🎯 Modo Examen Oficial FREC (Pearson VUE):**
   - Configura exámenes de **100 preguntas** (estándar estatal), **50 preguntas** (rápido) o el maratón de las **200 preguntas**.
   - Temporizador oficial regresivo de **3.5 horas** (o tiempo libre).
   - Opciones múltiples (A, B, C, D) barajadas dinámicamente.
   - Herramienta para **marcar preguntas (Flag for Review)** y rejilla interactiva de navegación directa.
   - Pantalla de resultados con nota final, estatus oficial (**Aprobado ≥ 75%**), animación de confetti y desglose por categorías.
   - Modo de revisión completa para auditar tus fallos con sus explicaciones legales.

2. **⚡ Modo Práctica Inmediata (Instant Feedback):**
   - Estudia pregunta a pregunta con corrección instantánea en verde/rojo.
   - Muestra de inmediato la **respuesta correcta oficial** y la **explicación legal FREC**.
   - Filtrable por cualquiera de las 19 categorías del programa.

3. **🗂️ Modo Flashcards 3D (Memorización Activa):**
   - Tarjetas interactivas con giro tridimensional.
   - **Frente:** Pregunta clave.
   - **Dorso:** Respuesta oficial verificada + notas explicativas.
   - Compatible con atajos de teclado (Barra espaciadora o Enter para voltear, flechas para avanzar).

4. **📖 Guía de Memorización & Buscador Rápido (200 Q&A):**
   - Vista completa de las 200 preguntas con sus respuestas idénticas a la guía de memorización.
   - **Buscador en tiempo real:** Escribe términos como `homestead`, `PITT`, `640 acres`, `escrow`, `defeasance`, etc., para encontrar preguntas al instante.
   - Botón para **ocultar respuestas**, ideal para auto-examinarse visualmente.

---

## 🌟 Características Adicionales
- **⭐ Sistema de Favoritos:** Guarda preguntas difíciles con la estrella para repasarlas por separado.
- **🌙 Modo Oscuro & Modo Claro:** Interfaz personalizable de alto contraste y descanso visual.
- **🔊 Efectos Sonoros:** Sonidos sutiles de acierto/error sintetizados con la Web Audio API (toggleable).
- **💾 Guardado Automático:** Guarda tus puntuaciones récord, preguntas marcadas y progreso en `localStorage`.
- **📱 100% Responsive:** Diseñado tanto para monitores de escritorio como para tablets y teléfonos móviles.
