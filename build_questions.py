import json

# Data definition for all 200 FREC questions
raw_questions = [
    # CORRETAJE (1-19)
    {
        "id": 1,
        "category": "Corretaje",
        "question": "Un broker recibe un cheque de earnest money de $10,000 un lunes. Según la ley de Florida, debe depositarlo en la cuenta de escrow a más tardar:",
        "answer": "Al final del tercer día hábil siguiente",
        "distractors": [
            "Inmediatamente antes de las 5:00 p.m. del mismo lunes",
            "Al final del siguiente día hábil (martes)",
            "Dentro de los 5 días hábiles siguientes a la aceptación"
        ],
        "explanation": "La regla de Florida estipula que el broker tiene hasta el final del tercer día hábil siguiente a la recepción del depósito por parte de su firma para depositarlo en la cuenta de escrow (los sales associates deben entregarlo al broker el siguiente día hábil)."
    },
    {
        "id": 2,
        "category": "Corretaje",
        "question": "Un broker usa dinero del escrow de un cliente para pagar la renta de su oficina, con intención de reponerlo. Esto es:",
        "answer": "Conversión (uso indebido), violación grave",
        "distractors": [
            "Commingling menor, permitido si se repone en 24 horas",
            "Una práctica aceptada si se cuenta con autorización verbal del arrendador",
            "Un préstamo temporal legal garantizado por la comisión futura"
        ],
        "explanation": "La conversión es el uso no autorizado o apropiación del dinero o propiedad de otra persona para beneficio propio del broker. Es un delito grave y causal de revocación de licencia."
    },
    {
        "id": 3,
        "category": "Corretaje",
        "question": "Toda publicidad de un sales associate en Florida debe mostrar:",
        "answer": "El nombre del brokerage registrado, de forma clara y visible",
        "distractors": [
            "Únicamente el nombre y número de teléfono celular del sales associate",
            "La dirección física completa de la oficina principal del broker",
            "El número de licencia de la DBPR tanto del agente como del broker"
        ],
        "explanation": "La ley de Florida exige que todo anuncio publicitario incluya el nombre comercial registrado o razón social de la firma de corretaje (brokerage)."
    },
    {
        "id": 4,
        "category": "Corretaje",
        "question": "Un asistente SIN licencia puede legalmente:",
        "answer": "Hacer trabajo administrativo: archivar, contestar teléfonos, repartir volantes",
        "distractors": [
            "Mostrar propiedades a clientes cuando el agente está ocupado",
            "Negociar comisiones o condiciones contractuales con el vendedor",
            "Celebrar open houses de manera independiente sin supervisión"
        ],
        "explanation": "Los asistentes sin licencia solo pueden realizar labores puramente administrativas y clericales, nunca actividades inmobiliarias que requieran licencia."
    },
    {
        "id": 5,
        "category": "Corretaje",
        "question": "Las comisiones que cobra un sales associate:",
        "answer": "Debe recibirlas únicamente a través de su broker empleador",
        "distractors": [
            "Puede cobrarlas directamente del vendedor si este firma un anexo",
            "Pueden ser pagadas directamente por la compañía de título al associate",
            "Pueden ser pagadas por cualquier broker registrado en el estado"
        ],
        "explanation": "Un sales associate o broker associate solo puede recibir compensación de corretaje directamente de su broker empleador registrado."
    },
    {
        "id": 6,
        "category": "Corretaje",
        "question": "Tres brokers de Miami acuerdan cobrar todos 6% de comisión para 'no dañarse el mercado'. Esto viola:",
        "answer": "Las leyes antimonopolio (antitrust / Sherman Act)",
        "distractors": [
            "La Ley de Vivienda Justa de 1968 (Fair Housing Act)",
            "La Ley RESPA sección 8 sobre comisiones compartidas",
            "El Estatuto de Fraudes de Florida (Statute of Frauds)"
        ],
        "explanation": "La fijación de precios (price-fixing) entre competidores es una conspiración ilegal que viola la Ley Sherman Antimonopolio."
    },
    {
        "id": 7,
        "category": "Corretaje",
        "question": "Bajo RESPA, Section 8, está prohibido:",
        "answer": "Pagar o recibir kickbacks (pagos por referidos) en transacciones con préstamo federal",
        "distractors": [
            "Cobrar comisiones variables según el volumen de ventas del mes",
            "Exigir un depósito en garantía mayor al 3% del precio de compra",
            "Ofrecer descuentos a compradores de primera vivienda"
        ],
        "explanation": "RESPA prohíbe pagar o recibir comisiones ilegales, comisiones ilícitas o compensaciones por referencias (kickbacks) en liquidaciones relacionadas con préstamos hipotecarios federamente asegurados."
    },
    {
        "id": 8,
        "category": "Corretaje",
        "question": "Un sales associate quiere cambiarse de brokerage. Lo correcto es:",
        "answer": "El nuevo broker registra el cambio ante la DBPR; el associate opera solo cuando queda registrado con el nuevo broker",
        "distractors": [
            "El associate continúa vendiendo con el número anterior por 60 días",
            "El associate notifica a la FREC por escrito en 30 días mientras sigue cerrando ventas",
            "El antiguo broker debe dar una carta de recomendación firmada ante notario"
        ],
        "explanation": "El cambio de empleador debe ser procesado con la DBPR antes de que el associate pueda prestar servicios bajo el nuevo corretaje."
    },
    {
        "id": 9,
        "category": "Corretaje",
        "question": "Un broker puede mantener el escrow:",
        "answer": "En la cuenta de escrow del brokerage, o el contrato puede designar a un abogado o compañía de título",
        "distractors": [
            "En la cuenta corriente personal del broker siempre que lleve un libro contable",
            "Únicamente en bonos del Tesoro de EE.UU. a corto plazo",
            "En una caja de seguridad bancaria en efectivo sellado"
        ],
        "explanation": "El depósito puede ser mantenido en una cuenta de depósito en garantía (escrow) del broker en un banco comercial, asociación de ahorro y préstamo o cooperativa de crédito en Florida, o en una compañía de título / abogado según lo designado en el contrato."
    },
    {
        "id": 10,
        "category": "Corretaje",
        "question": "El uso de un nombre comercial (trade name) por un brokerage en Florida requiere:",
        "answer": "Registrarlo ante la DBPR",
        "distractors": [
            "Publicarlo en el periódico local una vez por semana durante un mes",
            "Pagar una tasa federal de marca registrada a la FTC",
            "Aprobación de la Asociación de Realtors local (NAR)"
        ],
        "explanation": "Cualquier nombre ficticio o comercial que utilice una correduría debe registrarse debidamente ante el Departamento de Regulación Comercial y Profesional (DBPR)."
    },
    {
        "id": 11,
        "category": "Corretaje",
        "question": "¿Cuál de estas entidades SÍ puede registrarse como brokerage en Florida?",
        "answer": "Corporación, LLC o sociedad (partnership), además de persona natural",
        "distractors": [
            "Corporación de iglesia o religiosa exclusivamente",
            "Asociación comunitaria de condominios no incorporada",
            "Empresa de negocios conjuntos sin registro comercial"
        ],
        "explanation": "Las corporaciones con fines de lucro, compañías de responsabilidad limitada (LLC), sociedades colectivas y en comandita, así como personas naturales como propietarios únicos, pueden registrarse como firmas de corretaje de bienes raíces."
    },
    {
        "id": 12,
        "category": "Corretaje",
        "question": "Un 'personal assistant' CON licencia de sales associate, empleado por un sales associate:",
        "answer": "Puede hacer todo lo que hace un associate, pero su compensación la paga el associate que lo emplea a través del broker",
        "distractors": [
            "No puede realizar actividades inmobiliarias porque no tiene contrato con el cliente",
            "Recibe su pago en efectivo directamente del asistente principal sin conocimiento del broker",
            "Puede operar de manera independiente y cobrar comisiones sin intervención del broker"
        ],
        "explanation": "Un asistente con licencia puede realizar todas las actividades con licencia, pero cualquier compensación por servicios de corretaje debe ser canalizada y pagada a través del broker empleador."
    },
    {
        "id": 13,
        "category": "Corretaje",
        "question": "Un corredor recibió un depósito de 5.000$ de un comprador el martes a la 1:00 p. m., pero el vendedor no estará disponible hasta el lunes. El día bancario normal del corredor es el lunes. El corredor debe depositar los 5.000$ antes del final de:",
        "answer": "la jornada laboral del viernes.",
        "distractors": [
            "la jornada laboral del miércoles.",
            "la jornada laboral del jueves.",
            "el final del día del lunes siguiente."
        ],
        "explanation": "El broker tiene 3 días hábiles completos a partir del día siguiente a la recepción: miércoles (día 1), jueves (día 2), viernes (día 3). Debe depositarlo antes del final del horario bancario del viernes."
    },
    {
        "id": 14,
        "category": "Corretaje",
        "question": "Una persona cuyo trabajo es encontrar un inquilino para la propiedad y que cobra una cuota se conoce como:",
        "answer": "un agente de alquileres.",
        "distractors": [
            "un tasador hipotecario.",
            "un administrador fiduciario de hipotecas.",
            "un depositario en garantía."
        ],
        "explanation": "Un agente de alquileres (rental agent) actúa como intermediario para encontrar inquilinos a cambio de un honorario o comisión."
    },
    {
        "id": 15,
        "category": "Corretaje",
        "question": "Si una vendedora se niega a pagar la comisión a una corredora después de una venta residencial, la corredora puede:",
        "answer": "presentar una demanda ante los tribunales de justicia por su comisión.",
        "distractors": [
            "colocar un gravamen forzoso preventivo inmediato sobre el título de la propiedad residencial vendida",
            "revocar unilateralmente la escritura pública del comprador en el condado",
            "solicitar que la policía arreste al vendedor por fraude contractual"
        ],
        "explanation": "En transacciones residenciales, el corredor no puede colocar automáticamente un gravamen sobre la propiedad residencial por comisión no pagada; su recurso legal es demandar ante el tribunal civil."
    },
    {
        "id": 16,
        "category": "Corretaje",
        "question": "Una agente inmobiliaria recibió de un comprador un depósito en garantía de 5.000$. Inmediatamente entregó el depósito a su corredor. El corredor depositó el cheque el tercer día hábil en su cuenta general de operaciones.",
        "answer": "Este es un ejemplo de unificación de fondos de depósito en garantía.",
        "distractors": [
            "Esta es una práctica legal permitida hasta 10.000$.",
            "Es un procedimiento correcto de custodia de valores.",
            "Es una retención autorizada por la ley de Florida."
        ],
        "explanation": "La unificación indebida (commingling o mezcla de fondos) ocurre cuando se deposita dinero de garantía de un cliente en la cuenta operativa comercial o personal del broker."
    },
    {
        "id": 17,
        "category": "Corretaje",
        "question": "¿Cuánto dinero personal puede colocar un corredor en una cuenta de garantía de administración de propiedades?",
        "answer": "5.000$",
        "distractors": [
            "1.000$",
            "2.500$",
            "10.000$"
        ],
        "explanation": "La ley de Florida permite que el broker mantenga hasta $5,000 de sus fondos propios en una cuenta escrow de administración de propiedades (y hasta $1,000 en una de ventas) para pagar cargos bancarios."
    },
    {
        "id": 18,
        "category": "Corretaje",
        "question": "¿Qué afirmación es FALSA sobre la publicidad?",
        "answer": "Toda la publicidad debe llevar la dirección de la empresa.",
        "distractors": [
            "Toda la publicidad debe incluir el nombre comercial o razón social registrada del brokerage.",
            "Los anuncios ciegos (blind ads) están estrictamente prohibidos en Florida.",
            "Si se incluye el nombre del associate, debe figurar su apellido registrado."
        ],
        "explanation": "No es obligatorio que los anuncios lleven la dirección física completa de la oficina del broker; lo que sí es mandatorio es el nombre registrado de la firma de corretaje."
    },
    {
        "id": 19,
        "category": "Corretaje",
        "question": "Un inquilino potencial compró una lista de alquileres a un corredor y luego alquiló un dúplex que incluía según el anuncio todos los servicios públicos. El inquilino descubrió que solo se incluía agua en el alquiler y notificó al corredor dentro del plazo establecido. El inquilino tiene derecho a:",
        "answer": "100 % de la comisión pagada.",
        "distractors": [
            "75 % del dinero pagado por la lista.",
            "50 % únicamente por gastos de gestión.",
            "Ningún reembolso si visitó la propiedad voluntariamente."
        ],
        "explanation": "Si la información de la lista de alquileres es falsa o errónea en algún aspecto material, el cliente tiene derecho a demandar un reembolso del 100% de la tarifa pagada dentro de los 30 días."
    },

    # CONTRATOS (20-36)
    {
        "id": 20,
        "category": "Contratos",
        "question": "Para que un contrato de compraventa de bienes raíces sea exigible en Florida, el Statute of Frauds exige:",
        "answer": "Que esté por escrito y firmado por la parte contra la que se exige",
        "distractors": [
            "Que se entregue un depósito en efectivo superior al 5%",
            "Que sea protocolizado obligatoriamente ante dos notarios públicos",
            "Que esté registrado en los registros públicos del condado dentro de 24 horas"
        ],
        "explanation": "El Estatuto de Fraudes requiere que los contratos de compraventa de bienes raíces y los arrendamientos por más de un año estén por escrito y firmados para ser legalmente exigibles ante un tribunal."
    },
    {
        "id": 21,
        "category": "Contratos",
        "question": "Elementos esenciales de un contrato válido:",
        "answer": "Oferta y aceptación, consideración, partes capaces, objeto legal",
        "distractors": [
            "Depósito de arras, tasación bancaria, seguro de título y escritura",
            "Inspección previa, aprobación hipotecaria y firma ante testigos",
            "Oferta, contraoferta, comisión del corredor y entrega de posesión"
        ],
        "explanation": "Los 4 elementos esenciales para la validez de un contrato son: consentimiento mutuo (oferta y aceptación), causa o contraprestación válida (consideration), capacidad legal de las partes y legalidad del objeto."
    },
    {
        "id": 22,
        "category": "Contratos",
        "question": "En un exclusive right to sell listing:",
        "answer": "El broker cobra comisión aunque el dueño consiga al comprador",
        "distractors": [
            "El dueño vende por su cuenta y no le paga comisión al broker",
            "Cualquier broker competidor puede cobrar el 100% de la comisión",
            "Solo se cobra comisión si el precio de venta supera el precio listado"
        ],
        "explanation": "En el contrato de listado con derecho exclusivo de venta, el corredor tiene garantizada la comisión sin importar quién encuentre o procure al comprador, incluso el propio propietario."
    },
    {
        "id": 23,
        "category": "Contratos",
        "question": "En un option contract (contrato de opción):",
        "answer": "El optionor está obligado a vender si el optionee ejerce la opción; el optionee no está obligado a comprar (contrato unilateral)",
        "distractors": [
            "Ambas partes están mutuamente obligadas a cerrar la venta desde el primer día",
            "El optionee está forzado a comprar y el optionor puede negarse a vender",
            "Es un contrato bilateral que no requiere consideración de dinero"
        ],
        "explanation": "Un contrato de opción es unilateral: el concedente (optionor) está legalmente obligado a vender si el optante (optionee) ejerce la opción dentro del plazo convenido, pero el optante no está obligado a comprar."
    },
    {
        "id": 24,
        "category": "Contratos",
        "question": "Una contraoferta (counteroffer) legalmente significa:",
        "answer": "Rechazo de la oferta original y creación de una nueva oferta",
        "distractors": [
            "Aceptación condicional que mantiene en vigor los términos anteriores",
            "Modificación secundaria que la otra parte está obligada a aceptar",
            "Una suspensión temporal de 10 días para renegociar el precio"
        ],
        "explanation": "Una contraoferta anula y rechaza por completo la oferta original precedente, creando una propuesta contractual totalmente nueva."
    },
    {
        "id": 25,
        "category": "Contratos",
        "question": "El plazo de prescripción (statute of limitations) para demandar por incumplimiento de un contrato ESCRITO en Florida es:",
        "answer": "5 años",
        "distractors": [
            "4 años",
            "3 años",
            "7 años"
        ],
        "explanation": "En Florida, la ley de prescripción fija 5 años para contratos por escrito (y 4 años para contratos orales o verbales)."
    },
    {
        "id": 26,
        "category": "Contratos",
        "question": "Un sales associate en Florida puede:",
        "answer": "Llenar los formularios contractuales aprobados como parte de su trabajo como agente",
        "distractors": [
            "Redactar contratos desde cero y añadir cláusulas legales complejas",
            "Cobrar honorarios independientes por asesoría jurídica inmobiliaria",
            "Modificar los títulos de propiedad sin consentimiento de un abogado"
        ],
        "explanation": "Los licenciados de bienes raíces solo pueden completar formularios estandarizados aprobados (como contratos FAR/BAR); no pueden redactar instrumentos jurídicos ni dar asesoría legal (ejercicio no autorizado de la abogacía)."
    },
    {
        "id": 27,
        "category": "Contratos",
        "question": "Si el comprador incumple (default) y el contrato dice que el depósito queda como liquidated damages:",
        "answer": "El depósito es la compensación pactada y limita el reclamo del vendedor",
        "distractors": [
            "El vendedor puede retener el depósito y además demandar por daños y perjuicios ilimitados",
            "El depósito debe ser devuelto en su totalidad al comprador por ley",
            "La FREC retiene el depósito en el fondo de recuperación de fianzas"
        ],
        "explanation": "Los liquidated damages (daños liquidados o predeterminados) son el remedio contractual acordado de antemano que el vendedor acepta como compensación total si el comprador incumple."
    },
    {
        "id": 28,
        "category": "Contratos",
        "question": "Un contrato bilateral se caracteriza porque:",
        "answer": "Ambas partes se obligan mutuamente (promesa por promesa)",
        "distractors": [
            "Solo una de las partes hace una promesa vinculante",
            "Debe firmarse exclusivamente entre dos corredores de bolsa",
            "Requiere que intervengan dos abogados en el cierre"
        ],
        "explanation": "Un contrato bilateral se basa en un intercambio mutuo de promesas donde ambas partes adquieren obligaciones exigibles."
    },
    {
        "id": 29,
        "category": "Contratos",
        "question": "La cesión (assignment) de un contrato de compraventa:",
        "answer": "Es permitida salvo que el contrato la prohíba; el cedente sigue pudiendo ser responsable según lo pactado",
        "distractors": [
            "Está estrictamente prohibida por el Código Civil de Florida en todos los casos",
            "Libera automáticamente de toda obligación al comprador original sin novación",
            "Requiere la aprobación de la comisión FREC para tener validez"
        ],
        "explanation": "A menos que el contrato disponga lo contrario, los derechos contractuales se pueden ceder a un tercero, manteniendo el cedente responsabilidad subsidiaria si el cesionario no cumple."
    },
    {
        "id": 30,
        "category": "Contratos",
        "question": "Un buyer-broker agreement establece principalmente:",
        "answer": "Los términos de la relación entre el comprador y el broker: deberes, duración y compensación",
        "distractors": [
            "La hipoteca garantizada por el prestamista hacia el comprador",
            "El informe oficial de inspección física y vicios ocultos de la casa",
            "La póliza de seguro de título del condado"
        ],
        "explanation": "El acuerdo de corretaje con el comprador formaliza la relación de representación, los deberes del corredor, el plazo de vigencia y la forma en que será compensado."
    },
    {
        "id": 31,
        "category": "Contratos",
        "question": "¿Cuál de estos contratos debe estar por escrito para ser exigible en Florida?",
        "answer": "Un contrato de compraventa de una casa",
        "distractors": [
            "Un contrato de arrendamiento residencial por 6 meses",
            "Un acuerdo de listado abierto verbal menor a un año",
            "Un acuerdo de división de comisiones entre dos agentes de la misma firma"
        ],
        "explanation": "Bajo el Statute of Frauds, las transferencias de bienes raíces (como la venta de una vivienda) deben ser por escrito para tener fuerza ejecutoria."
    },
    {
        "id": 32,
        "category": "Contratos",
        "question": "El incumplimiento de la ley contra el fraude (o antifraude) dará lugar a:",
        "answer": "un contrato inejecutable.",
        "distractors": [
            "un contrato nulo de pleno derecho automáticamente sin necesidad de juicio.",
            "la cárcel inmediata de los firmantes por delito penal grave.",
            "un contrato ejecutable si ambas partes prestan juramento ante el broker."
        ],
        "explanation": "Un contrato que incumple el Estatuto de Fraudes (por ejemplo, ser verbal cuando la ley exige que sea escrito) es válido entre las partes si voluntariamente lo cumplen, pero es inejecutable (unenforceable) ante un tribunal si una parte rehúsa cumplirlo."
    },
    {
        "id": 33,
        "category": "Contratos",
        "question": "Un inquilino firmó un contrato de arrendamiento por 10 años con un alquiler mensual base de 1.900$, más el 2% del volumen bruto mensual de ventas superiores a los 95.000$. El inquilino también debe pagar todos los impuestos sobre la propiedad, seguros y otros costos que normalmente se consideran costos del propietario. ¿Qué tipo de arrendamiento tiene el inquilino?",
        "answer": "Un arrendamiento neto.",
        "distractors": [
            "Un arrendamiento bruto (gross lease).",
            "Un arrendamiento de superficie (ground lease).",
            "Un subarrendamiento residencial."
        ],
        "explanation": "En un arrendamiento neto (net lease), el arrendatario asume el pago de algunos o todos los gastos operativos de la propiedad (como impuestos, seguros y mantenimiento) además de la renta base estipulada."
    },
    {
        "id": 34,
        "category": "Contratos",
        "question": "¿Qué elemento NO es esencial en un contrato de venta de bienes raíces válido?",
        "answer": "El depósito en garantía.",
        "distractors": [
            "La consideración legal (contraprestación).",
            "El consentimiento y acuerdo mutuo de las partes.",
            "La capacidad jurídica de los firmantes."
        ],
        "explanation": "Un depósito en garantía (earnest money deposit) no es un requisito legal indispensable para la existencia o validez de un contrato vinculante, aunque es habitual en la práctica comercial."
    },
    {
        "id": 35,
        "category": "Contratos",
        "question": "La ley de prescripción establece:",
        "answer": "el período de tiempo en el que puede ejecutarse un contrato.",
        "distractors": [
            "los requisitos formales para inscribir una escritura pública.",
            "la tasa de interés máxima que puede cobrar un prestamista privado.",
            "el porcentaje de comisión obligatorio en los contratos de corretaje."
        ],
        "explanation": "El Statute of Limitations determina el plazo legal límite dentro del cual una parte agraviada puede entablar una demanda judicial para exigir derechos contractuales."
    },
    {
        "id": 36,
        "category": "Contratos",
        "question": "Cuando las partes en un contrato declaran las condiciones del contrato y muestran sus intenciones ya sea oralmente o por escrito, ¿qué tipo de contrato se ha creado?",
        "answer": "Expresa.",
        "distractors": [
            "Implícito.",
            "Ficticio.",
            "Formal de sello lacrado."
        ],
        "explanation": "Un contrato expreso (express contract) se forma cuando los términos y acuerdos se manifiestan explícitamente con palabras, ya sea de forma hablada o escrita."
    },

    # HIPOTECAS (37-60)
    {
        "id": 37,
        "category": "Hipotecas",
        "question": "La diferencia clave entre un préstamo FHA y uno VA es:",
        "answer": "El FHA está asegurado (insured) por el gobierno federal; el VA está garantizado (guaranteed) para veteranos elegibles",
        "distractors": [
            "El FHA es emitido directamente por el presidente y el VA por bancos privados",
            "El VA requiere un 20% de pago inicial obligatorio y el FHA cero inicial",
            "El préstamo FHA está reservado exclusivamente a personal militar en activo"
        ],
        "explanation": "FHA asegura préstamos emitidos por prestamistas aprobados, mientras que el Departamento de Asuntos de Veteranos (VA) ofrece una garantía parcial del préstamo para veteranos calificados sin exigir enganche."
    },
    {
        "id": 38,
        "category": "Hipotecas",
        "question": "La cláusula de acceleration permite al prestamista:",
        "answer": "Declarar vencido el saldo total ante el incumplimiento del prestatario",
        "distractors": [
            "Acelerar la entrega de las llaves al día del contrato preliminar",
            "Aumentar discrecionalmente la tasa de interés en cualquier momento",
            "Exigir el pago anticipado sin ninguna penalización para el comprador"
        ],
        "explanation": "La cláusula de aceleración autoriza al acreedor hipotecario a declarar exigible de inmediato la totalidad de la deuda restante si el deudor incurre en mora o falta de pago."
    },
    {
        "id": 39,
        "category": "Hipotecas",
        "question": "La cláusula due-on-sale (alienation) establece que:",
        "answer": "Si se transfiere la propiedad, el prestamista puede exigir el pago total del préstamo",
        "distractors": [
            "El comprador puede transferir la hipoteca sin aprobación del banco",
            "El vendedor debe pagar una multa al comprador si vende antes de 5 años",
            "El préstamo se cancela automáticamente con el fallecimiento del vendedor"
        ],
        "explanation": "La cláusula de enajenación o debido a la venta impide que el prestatario transfiera la propiedad con la hipoteca vigente sin antes cancelar la deuda por completo o tener aprobación expresa del prestamista."
    },
    {
        "id": 40,
        "category": "Hipotecas",
        "question": "La cláusula de defeasance en una hipoteca significa:",
        "answer": "Que el gravamen se extingue cuando el prestatario paga totalmente la deuda",
        "distractors": [
            "Que el prestamista puede embargar la propiedad sin orden judicial previa",
            "Que la deuda se transfiere a los herederos automáticamente sin trámite",
            "Que el título queda en fideicomiso a perpetuidad"
        ],
        "explanation": "La cláusula de revocación o defeasance anula el gravamen del prestamista una vez que todas las obligaciones de pago de la nota hipotecaria han sido completamente saldadas."
    },
    {
        "id": 41,
        "category": "Hipotecas",
        "question": "En los primeros años de un préstamo amortizado a 30 años, la mayor parte de cada pago mensual corresponde a:",
        "answer": "Intereses",
        "distractors": [
            "Reducción directa del capital principal",
            "Impuestos sobre la propiedad ad valorem",
            "Seguro contra riesgos catastróficos"
        ],
        "explanation": "En un préstamo de amortización constante a tipo fijo a 30 años, en los primeros años el saldo de la deuda es elevado, por lo que casi todo el pago se consume en intereses devengados."
    },
    {
        "id": 42,
        "category": "Hipotecas",
        "question": "Un préstamo con amortización a 30 años pero vencimiento total (balloon) a los 10 años se llama:",
        "answer": "Balloon loan (parcialmente amortizado)",
        "distractors": [
            "Préstamo totalmente amortizado convencional",
            "Préstamo de capital negativo invertido",
            "Hipoteca de presupuesto ajustable (ARM)"
        ],
        "explanation": "Un préstamo parcialmente amortizado tiene cuotas calculadas sobre un plazo más largo (ej. 30 años), pero vence antes (ej. 10 años), requiriendo un pago final considerable (pago globo o balloon)."
    },
    {
        "id": 43,
        "category": "Hipotecas",
        "question": "El seguro hipotecario privado (PMI) en un préstamo convencional típicamente se exige cuando:",
        "answer": "El LTV supera el 80% (down payment menor al 20%)",
        "distractors": [
            "El comprador tiene un puntaje de crédito FICO superior a 750",
            "La casa es una residencia secundaria vacacional",
            "El valor de la propiedad supera el millón de dólares"
        ],
        "explanation": "Los prestamistas convencionales requieren seguro PMI para protegerse contra el incumplimiento cuando el ratio préstamo-valor (LTV) excede el 80% (es decir, el comprador aporta menos del 20% de pago inicial)."
    },
    {
        "id": 44,
        "category": "Hipotecas",
        "question": "En una asunción (assumption) de hipoteca con novation:",
        "answer": "El comprador asume la deuda y el vendedor queda liberado de responsabilidad",
        "distractors": [
            "El vendedor sigue siendo el deudor solidario responsable si el comprador no paga",
            "El banco cobra doble interés mensual durante el primer año",
            "Se cancela la hipoteca existente y se emite un bono público del estado"
        ],
        "explanation": "La novación legal (novation) sustituye al vendedor por el nuevo comprador en la obligación crediticia, liberando al deudor original de toda responsabilidad futura."
    },
    {
        "id": 45,
        "category": "Hipotecas",
        "question": "Bajo Truth in Lending (Regulation Z), el prestamista debe divulgar:",
        "answer": "La APR (tasa de porcentaje anual) y el costo total del crédito",
        "distractors": [
            "La ganancia neta estimada del corredor de bienes raíces",
            "El valor catastral futuro proyectado a 10 años",
            "La comisión total que recibe la aseguradora de título"
        ],
        "explanation": "El objetivo principal de la Ley TILA (Regulación Z) es garantizar que los consumidores conozcan el costo financiero verdadero del crédito, expresado a través de la Tasa de Porcentaje Anual (APR)."
    },
    {
        "id": 46,
        "category": "Hipotecas",
        "question": "¿Qué acción NO es un requisito de la norma integrada de divulgación TILA-RESPA (TRID)?",
        "answer": "Entregar al solicitante de la hipoteca una lista de prestamistas competidores para que pueda comparar la mejor tasa de interés.",
        "distractors": [
            "Entregar la Estimación del Préstamo (Loan Estimate) dentro de los 3 días hábiles posteriores a la solicitud.",
            "Proporcionar la Divulgación de Cierre (Closing Disclosure) al menos 3 días hábiles antes del cierre.",
            "Divulgar todos los costos de cierre y cargos de originación detallados."
        ],
        "explanation": "TRID no exige a los prestamistas que provean una lista de entidades competidoras; exige divulgar con transparencia y exactitud las condiciones y costos del préstamo propio mediante el Loan Estimate y Closing Disclosure."
    },
    {
        "id": 47,
        "category": "Hipotecas",
        "question": "La ley que le exige al prestamista comunicar a los consumidores la tasa porcentual anual es la:",
        "answer": "Ley de Transparencia (o Veracidad) en los Préstamos.",
        "distractors": [
            "Ley de Procedimientos de Liquidación de Bienes Raíces (RESPA).",
            "Ley de Vivienda Justa de los Estados Unidos.",
            "Ley de Igualdad de Oportunidades de Empleo (EEOC)."
        ],
        "explanation": "La Ley Truth in Lending Act (TILA) obliga a los prestamistas a comunicar claramente la tasa de porcentaje anual (APR) y los costos de financiamiento."
    },
    {
        "id": 48,
        "category": "Hipotecas",
        "question": "¿Qué cláusula se incluye en una hipoteca para evitar que un comprador posterior asuma un préstamo hipotecario?",
        "answer": "Cláusula de cancelamiento por venta (due-on-sale)",
        "distractors": [
            "Cláusula de subordinación condicional.",
            "Cláusula de rescate anticipado (equitable redemption).",
            "Cláusula de defeasance automática."
        ],
        "explanation": "La cláusula due-on-sale o cláusula de aceleración por venta otorga al prestamista la opción de exigir la cancelación íntegra del préstamo en caso de venta o transferencia del inmueble."
    },
    {
        "id": 49,
        "category": "Hipotecas",
        "question": "¿Qué entidad es un prestamista hipotecario primario que NO acepta depósitos en persona (o a la vista)?",
        "answer": "Prestamistas hipotecarios (Mortgage Companies / Mortgage Bankers).",
        "distractors": [
            "Bancos comerciales nacionales.",
            "Asociaciones de ahorros y préstamos locales.",
            "Cooperativas de crédito federales."
        ],
        "explanation": "Las empresas prestamistas hipotecarias no son instituciones de depósito; originan y financian préstamos usando líneas de crédito o fondos propios pero no aceptan depósitos de clientes."
    },
    {
        "id": 50,
        "category": "Hipotecas",
        "question": "Las personas que solicitan préstamos hipotecarios, aceptan solicitudes de préstamos hipotecarios y negocian los términos de nuevos préstamos hipotecarios en nombre de un prestatario se llaman:",
        "answer": "originadores de préstamos hipotecarios (Mortgage Loan Originators - MLO).",
        "distractors": [
            "tasadores de bienes raíces certificados.",
            "administradores de propiedades residenciales.",
            "corredores de seguros de título de propiedad."
        ],
        "explanation": "Los originadores de préstamos hipotecarios (MLO) tienen licencia para asesorar prestatarios, procesar solicitudes y negociar términos hipotecarios."
    },
    {
        "id": 51,
        "category": "Hipotecas",
        "question": "Una disposición en todas las hipotecas que permite al deudor hipotecario moroso evitar la ejecución hipotecaria haciendo todos los pagos atrasados de la hipoteca, las penalizaciones por morosidad y los costos de cobro hasta el momento de la venta por ejecución hipotecaria es:",
        "answer": "una cláusula de derecho a restablecer (right to reinstate).",
        "distractors": [
            "una cláusula de renuncia a juicio rápido.",
            "una cláusula de novación automática del gravamen.",
            "una cláusula de retención de depósito en garantía."
        ],
        "explanation": "El derecho de restitución o restablecimiento concede al deudor la facultad de subsanar el incumplimiento pagando todas las sumas pendientes antes de la subasta judicial."
    },
    {
        "id": 52,
        "category": "Hipotecas",
        "question": "¿Qué ley federal estableció que la publicidad engañosa es un delito federal?",
        "answer": "Ley de transparencia o veracidad en los préstamos (TILA)",
        "distractors": [
            "Ley Patriota de los Estados Unidos.",
            "Ley Sherman Antimonopolio de 1890.",
            "Ley Dodd-Frank sobre Fondos Comunes."
        ],
        "explanation": "La TILA (y la Regulación Z) sanciona severamente la publicidad engañosa sobre créditos y tasas hipotecarias."
    },
    {
        "id": 53,
        "category": "Hipotecas",
        "question": "¿Qué participante del mercado secundario garantiza préstamos asegurados y garantizados por el gobierno?",
        "answer": "Ginnie Mae (Government National Mortgage Association)",
        "distractors": [
            "Fannie Mae (FNMA).",
            "Freddie Mac (FHLMC).",
            "Sallie Mae."
        ],
        "explanation": "Ginnie Mae es una corporación del gobierno que respalda títulos garantizados con hipotecas aseguradas por FHA o garantizadas por VA."
    },
    {
        "id": 54,
        "category": "Hipotecas",
        "question": "Un estado de teoría del título es aquel en el que una hipoteca:",
        "answer": "transfiere el título al prestamista o agente de depósito en garantía hasta que se pague el préstamo.",
        "distractors": [
            "deja el título legal en manos del comprador desde el primer día reteniendo solo un gravamen.",
            "prohíbe que el banco ejecute la propiedad ante un impago.",
            "transfiere la propiedad directamente al Estado en caso de venta."
        ],
        "explanation": "En la teoría del título (Title Theory), el prestamista mantiene la titularidad legal hasta que la deuda se liquide. En Florida rige la teoría del gravamen (Lien Theory), donde el deudor conserva el título legal."
    },
    {
        "id": 55,
        "category": "Hipotecas",
        "question": "¿Qué término define una situación en la que, durante los primeros años de un préstamo, el saldo del capital aumenta?",
        "answer": "Amortización negativa.",
        "distractors": [
            "Amortización acelerada.",
            "Depreciación acumulada de mercado.",
            "Apalancamiento de rendimiento cero."
        ],
        "explanation": "La amortización negativa ocurre cuando los pagos mensuales no cubren los intereses devengados, y la diferencia se suma al saldo principal de la deuda."
    },
    {
        "id": 56,
        "category": "Hipotecas",
        "question": "¿Cuál de las siguientes declaraciones es VERDADERA sobre los pagos mensuales de un préstamo amortizado a 30 años?",
        "answer": "Inicialmente, el interés es la mayor parte del pago.",
        "distractors": [
            "Desde el primer año el 80% va directamente a amortizar capital.",
            "Los pagos mensuales aumentan un 10% anualmente de forma obligatoria.",
            "No se pagan intereses durante los primeros 5 años de gracia."
        ],
        "explanation": "Debido a la magnitud del saldo no amortizado inicial, la cuota mensual se destina principalmente a cubrir intereses durante los primeros períodos del cronograma."
    },
    {
        "id": 57,
        "category": "Hipotecas",
        "question": "Un comprador que obtiene un préstamo hipotecario que cubre la compra de un condominio más muebles, electrodomésticos y otros bienes muebles, como toallas y utensilios de cocina, tiene:",
        "answer": "una hipoteca combinada (package mortgage).",
        "distractors": [
            "una hipoteca global (blanket mortgage).",
            "una hipoteca de envoltura (wraparound mortgage).",
            "una hipoteca de valor acumulado (HELOC)."
        ],
        "explanation": "Una hipoteca combinada (package mortgage) financia simultáneamente bienes raíces (propiedad inmobiliaria) y bienes personales muebles (personal property)."
    },
    {
        "id": 58,
        "category": "Hipotecas",
        "question": "Una hipoteca en la que los cambios en la tasa de interés pueden causar cambios en el monto del pago mensual se llama:",
        "answer": "hipoteca con tasa ajustable (ARM - Adjustable Rate Mortgage).",
        "distractors": [
            "hipoteca con tasa fija amortizada a 15 años.",
            "hipoteca de pago inverso o reversa.",
            "hipoteca de compra a término fijo."
        ],
        "explanation": "Las hipotecas de tasa ajustable (ARM) fluctúan según un índice financiero de referencia más un margen fijado por el prestamista."
    },
    {
        "id": 59,
        "category": "Hipotecas",
        "question": "Un profesor universitario jubilado tiene 72 años. El prestamista local al que el profesor solicitó una hipoteca a 30 años negó su solicitud, a pesar de que tiene suficientes ingresos de su plan de pensiones y un excelente historial crediticio.",
        "answer": "Las acciones del prestamista violan la Ley de Igualdad de Oportunidades de Crédito (ECOA).",
        "distractors": [
            "El prestamista actuó correctamente porque a los 72 años no vivirá 30 años.",
            "Las acciones son legales según las normas de suscripción de Fannie Mae.",
            "La denegación está autorizada bajo las leyes estatales de usura bancaria."
        ],
        "explanation": "La Ley ECOA prohíbe la discriminación de solicitantes de crédito por motivos de edad, raza, religión, sexo o procedencia de ingresos públicos."
    },
    {
        "id": 60,
        "category": "Hipotecas",
        "question": "Un posible prestatario solicita un préstamo convencional de interés fijo. El ingreso bruto mensual del prestatario es de 6.500$. El Pago de Capital, Intereses, Impuestos y Seguro (PITI) mensual proyectado es de 1.372$, la Prima de Seguro Hipotecarios (MIP) es de 150$ y, según un informe de crédito, el prestatario tiene las siguientes obligaciones a largo plazo: Pago del automóvil: 400$ Préstamo estudiantil: 390$ Tarjetas de crédito: 250$ ¿Cuál es el porcentaje total de obligaciones del prestatario? ¿Cumple con el margen de porcentaje requerido por el prestamista para un préstamo hipotecario convencional?",
        "answer": "0,3941 o el 39,4 % de TOR es más que el umbral de TOR para un préstamo convencional",
        "distractors": [
            "28,0 % de TOR, lo cual cumple holgadamente con los requisitos estándar",
            "33,5 % de TOR, que es exactamente igual al límite máximo permitido",
            "45,2 % de TOR, lo cual califica automáticamente para aprobación FHA"
        ],
        "explanation": "Gastos totales: 1,372 + 150 + 400 + 390 + 250 = 2,562$. TOR = 2,562 / 6,500 = 0.3941 (39.4%). En préstamos convencionales el estándar suele ser 36%, por lo que supera el umbral."
    },

    # PROPIEDAD (61-73)
    {
        "id": 61,
        "category": "Propiedad",
        "question": "El bundle of rights (conjunto de derechos de propiedad) incluye:",
        "answer": "Disposition, exclusion, enjoyment, possession y control (DEEP C)",
        "distractors": [
            "Deed, easement, equity, police power y confiscation",
            "Dominio, expropiación, gravamen, venta e hipoteca",
            "Duración, evasión, ejecución, posesión y cesión"
        ],
        "explanation": "El acrónimo DEEP C resume el haz de derechos legales de propiedad: Disposición, Exclusión, Goce/Disfrute, Posesión y Control."
    },
    {
        "id": 62,
        "category": "Propiedad",
        "question": "Un life estate termina:",
        "answer": "Con la muerte del life tenant (o de la persona cuya vida mide el estate)",
        "distractors": [
            "A los 30 años de su otorgamiento por la ley de prescripción",
            "Cuando el beneficiario vende su derecho a un tercero",
            "Si la propiedad no se asegura contra incendios en 90 días"
        ],
        "explanation": "Un patrimonio de por vida (life estate) es un derecho de propiedad limitado en el tiempo que se extingue al fallecer la persona sobre cuya vida está medido el patrimonio."
    },
    {
        "id": 63,
        "category": "Propiedad",
        "question": "Para crear un joint tenancy con derecho de supervivencia se requieren las cuatro unidades (PITT):",
        "answer": "Possession, interest, time y title (posesión, interés, tiempo y título)",
        "distractors": [
            "Price, insurance, taxes y tenure",
            "Property, investment, trade y tenancy",
            "Protection, inheritance, term y taxation"
        ],
        "explanation": "Las cuatro unidades indispensables (PITT) son: Posesión (igual uso), Interés (igual cuota), Tiempo (creado simultáneamente) y Título (mismo instrumento)."
    },
    {
        "id": 64,
        "category": "Propiedad",
        "question": "En un tenancy in common:",
        "answer": "Cada dueño tiene una participación divisible y heredable, que puede ser desigual",
        "distractors": [
            "Existe derecho de supervivencia obligatorio entre los co-propietarios",
            "Todos los dueños deben tener obligatoriamente el mismo porcentaje exacto",
            "Al morir un co-propietario, su cuota pasa al socio sobreviviente"
        ],
        "explanation": "El arrendamiento o copropiedad en común no tiene derecho de supervivencia; las partes pueden tener cuotas desiguales y al fallecer la porción pasa a los herederos o beneficiarios testamentarios."
    },
    {
        "id": 65,
        "category": "Propiedad",
        "question": "La protección del homestead en Florida contra acreedores forzosos significa que:",
        "answer": "La residencia principal tiene protección amplia contra la venta forzosa por la mayoría de las deudas",
        "distractors": [
            "El propietario queda exento de pagar impuestos a la propiedad inmobiliaria",
            "El banco hipotecario no puede ejecutar la casa en caso de no pagar el préstamo",
            "La casa nunca puede ser vendida ni embargada por el gobierno bajo ninguna ley"
        ],
        "explanation": "El artículo X de la Constitución de Florida protege la residencia principal contra la venta forzosa por deudas personales de tarjetas, juicios médicos, etc. (con excepciones como hipotecas, impuestos a la propiedad e hipotecas de mecánicos)."
    },
    {
        "id": 66,
        "category": "Propiedad",
        "question": "La diferencia principal entre condominio y cooperativa es:",
        "answer": "En el condominio se posee la unidad en fee simple más un interés en las áreas comunes; en la cooperativa se poseen acciones de la corporación con derecho de ocupación",
        "distractors": [
            "En el condominio se es dueño de acciones y en la cooperativa se tiene título de escritura individual",
            "Los condominios son únicamente comerciales y las cooperativas residenciales",
            "En la cooperativa no se pagan gastos de mantenimiento mensuales"
        ],
        "explanation": "En el condominio se es propietario en fee simple de la unidad individual más porcentaje proindiviso de áreas comunes. En una cooperativa la corporación es dueña del edificio y los residentes poseen acciones con un arrendamiento propietario."
    },
    {
        "id": 67,
        "category": "Propiedad",
        "question": "Un time-sharing otorga:",
        "answer": "Derecho de uso de la unidad por un período recurrente cada año",
        "distractors": [
            "La posesión absoluta durante los 12 meses continuos de la unidad",
            "Propiedad exclusiva de todo el complejo turístico",
            "El derecho a subarrendar sin pagar la cuota de mantenimiento"
        ],
        "explanation": "El tiempo compartido fracciona el uso y goce de la unidad vacacional en intervalos de tiempo preestablecidos anualmente."
    },
    {
        "id": 68,
        "category": "Propiedad",
        "question": "La adhesión (adquisición por causas naturales, como sedimento de un río) es un ejemplo de:",
        "answer": "Adquisición por accesión natural del título",
        "distractors": [
            "Alienación involuntaria por prescripción judicial",
            "Expropiación forzosa por servidumbre pública",
            "Transferencia por sucesión intestada"
        ],
        "explanation": "La accesión (aluvión/acreción) es el incremento natural de terreno por el depósito paulatino de sedimentos causados por el agua."
    },
    {
        "id": 69,
        "category": "Propiedad",
        "question": "¿Qué información debe darse al comprador de unidades de condominios residenciales nuevos y de reventa?",
        "answer": "Una declaración de condominio.",
        "distractors": [
            "Una copia de los impuestos sobre la renta del constructor de los últimos 5 años.",
            "Una fianza bancaria irrevocable de 100.000$.",
            "La lista completa de todos los inquilinos morosos del complejo."
        ],
        "explanation": "Tanto para unidades nuevas como en reventa, la ley exige entregar los documentos de gobierno del condominio, incluida la Declaración de Condominio, artículos y estatutos."
    },
    {
        "id": 70,
        "category": "Propiedad",
        "question": "¿Qué declaración sobre la copropiedad conyugal (tenancy by the entireties) es FALSA?",
        "answer": "La escritura debe indicar específicamente la intención de crear tal copropiedad conyugal.",
        "distractors": [
            "Se crea automáticamente cuando un matrimonio adquiere una propiedad conjuntamente sin especificar otra forma.",
            "Incluye el derecho intrínseco de supervivencia entre los cónyuges.",
            "Ninguno de los cónyuges puede gravar la propiedad sin el consentimiento del otro."
        ],
        "explanation": "En Florida, si un hombre y una mujer casados compran una propiedad juntos, se presume por derecho consuetudinario que forman un Tenancy by the Entireties sin necesidad de cláusulas expresas complejas."
    },
    {
        "id": 71,
        "category": "Propiedad",
        "question": "Un hombre tiene una granja en dominio pleno y la cede a un amigo hasta su muerte, momento en el que una mujer adquirirá el título de dominio pleno de la granja. El interés de la mujer en la granja es un:",
        "answer": "dominio remanente (remainder estate).",
        "distractors": [
            "patrimonio en reversión (reversionary interest).",
            "patrimonio en tenencia precaria.",
            "dominio condicionado resolutorio."
        ],
        "explanation": "Cuando un patrimonio de por vida vence y la propiedad pasa a un tercero designado que no es el otorgante original, dicho tercero tiene un interés de dominio remanente (remainderman)."
    },
    {
        "id": 72,
        "category": "Propiedad",
        "question": "El conjunto de derechos legales asociados a la propiedad inmobiliaria NO incluye el derecho de:",
        "answer": "intención.",
        "distractors": [
            "disposición.",
            "exclusión.",
            "posesión."
        ],
        "explanation": "El bundle of rights abarca disposición, goce, exclusión, posesión y control (DEEP C). 'Intención' no es un derecho de propiedad."
    },
    {
        "id": 73,
        "category": "Propiedad",
        "question": "¿Qué patrimonio incluye el derecho de supervivencia?",
        "answer": "Posesión conjunta (Joint Tenancy).",
        "distractors": [
            "Tenencia en común (Tenancy in Common).",
            "Arrendamiento a voluntad por meses.",
            "Patrimonio por tolerancia (Tenancy at sufferance)."
        ],
        "explanation": "La posesión o tenencia conjunta (Joint Tenancy with right of survivorship) se distingue por el derecho de supervivencia entre los copropietarios."
    },

    # VALUACIÓN (74-90)
    {
        "id": 74,
        "category": "Valuación",
        "question": "El enfoque más confiable para valuar una vivienda unifamiliar es:",
        "answer": "Comparación de ventas (sales comparison approach)",
        "distractors": [
            "Enfoque de costos de depreciación contable",
            "Enfoque de capitalización neta de ingresos brutos",
            "Método de flujo de caja libre descontado"
        ],
        "explanation": "Para residencias unifamiliares y lotes residenciales, el método comparativo de ventas es el más directo y confiable del mercado."
    },
    {
        "id": 75,
        "category": "Valuación",
        "question": "Fórmula del enfoque de ingresos (income capitalization):",
        "answer": "Valor = Ingreso neto operativo / tasa de capitalización (V = I / R)",
        "distractors": [
            "Valor = Ingreso bruto efectivo x tasa de amortización (V = I x R)",
            "Valor = Costo de reposición / factor multiplicador de renta",
            "Valor = Utilidad neta antes de impuestos + depreciación fiscal"
        ],
        "explanation": "La fórmula fundamental de capitalización inmobiliaria es V = I / R (Valor = NOI / Cap Rate)."
    },
    {
        "id": 76,
        "category": "Valuación",
        "question": "En el enfoque de costo: Valor =",
        "answer": "Costo de reemplazo nuevo - depreciación + valor del terreno",
        "distractors": [
            "Costo de adquisición histórica + mejoras no amortizadas",
            "Valor del terreno - costo de demolición + precio de mercado",
            "Costo de construcción original x inflación acumulada"
        ],
        "explanation": "El método del costo calcula cuánto costaría reproducir/reemplazar las mejoras nuevas, deduce la depreciación física, funcional y económica acumulada, y suma el valor no depreciado del terreno."
    },
    {
        "id": 77,
        "category": "Valuación",
        "question": "La pérdida de valor por una planta industrial ruidosa construida al lado es:",
        "answer": "Obsolescencia económica (externa)",
        "distractors": [
            "Deterioro físico curable",
            "Obsolescencia funcional incurable",
            "Depreciación ordinaria de uso"
        ],
        "explanation": "La obsolescencia externa o económica proviene de factores ambientales, vecinales o externos a la propiedad que están fuera del control del dueño, y casi siempre es incurable."
    },
    {
        "id": 78,
        "category": "Valuación",
        "question": "Un CMA (Comparative Market Analysis):",
        "answer": "Lo prepara el agente para estimar precio de mercado; no es un appraisal",
        "distractors": [
            "Es una tasación formal que debe cumplir con las normas estrictas de USPAP",
            "Lo realiza un tasador certificado por la junta estatal de tasadores",
            "Es un informe hipotecario obligatorio para obtener préstamos FHA"
        ],
        "explanation": "Un análisis comparativo de mercado (CMA) es una herramienta de orientación de precios preparada por un corredor o agente inmobiliario para ayudar al vendedor o comprador, y no debe presentarse como un informe de tasación oficial."
    },
    {
        "id": 79,
        "category": "Valuación",
        "question": "El principio de sustitución (substitution) dice que:",
        "answer": "El comprador no pagará más por una propiedad que el costo de otra igualmente deseable",
        "distractors": [
            "El valor siempre aumenta en proporción directa con el crecimiento del PIB",
            "Las propiedades más antiguas reemplazan el valor de las recién construidas",
            "Cualquier modificación arquitectónica incrementa el valor en 100% de su coste"
        ],
        "explanation": "El principio de sustitución sostiene que el valor máximo de un bien inmueble está fijado por el costo de adquisición de una propiedad alternativa sustituta con similar utilidad y atractivo."
    },
    {
        "id": 80,
        "category": "Valuación",
        "question": "Highest and best use (mejor y mayor uso) es:",
        "answer": "El uso legalmente permitido, físicamente posible y financieramente viable que da el mayor valor",
        "distractors": [
            "El uso que genera la mayor cantidad de impuestos al gobierno local",
            "El uso residencial de mayor densidad sin importar las ordenanzas",
            "El uso histórico que ha tenido el suelo en los últimos 50 años"
        ],
        "explanation": "El mayor y mejor uso es el uso más rentable y productivo que cumple con las cuatro pruebas: legalmente permisible, físicamente posible, financieramente viable y de máxima productividad."
    },
    {
        "id": 81,
        "category": "Valuación",
        "question": "USPAP son:",
        "answer": "Los estándares uniformes de práctica profesional de valuación que debe seguir el appraiser",
        "distractors": [
            "Las pautas de inspección de edificios contra huracanes de Florida",
            "El código ético de la Asociación Nacional de Corredores (NAR)",
            "Las regulaciones de zonificación y planificación urbana del condado"
        ],
        "explanation": "USPAP (Uniform Standards of Professional Appraisal Practice) son los estándares éticos y metodológicos nacionales obligatorios que rigen la actividad de los tasadores profesionales."
    },
    {
        "id": 82,
        "category": "Valuación",
        "question": "¿Qué gasto se resta para obtener el Ingreso Operativo Neto (NOI)?",
        "answer": "Pérdidas por desocupación y alquileres no cobrados",
        "distractors": [
            "El servicio de la deuda (pago de hipoteca / intereses)",
            "El impuesto sobre la renta personal de los inversionistas",
            "La amortización de costo fiscal y dividendos pagados"
        ],
        "explanation": "El NOI se calcula restando del Ingreso Bruto Potencial (PGI) las pérdidas por vacancia e incobrables (V&C) para obtener el Ingreso Bruto Efectivo (EGI), y deduciendo luego los gastos operativos (OE). El servicio de la deuda no se incluye en el NOI."
    },
    {
        "id": 83,
        "category": "Valuación",
        "question": "Una propiedad comparable tiene un dormitorio más (8.000$) y un lote ligeramente más grande (2.000$) que la propiedad en cuestión o sujeta a comparación. El análisis comparativo de mercado requiere un ajuste neto de:",
        "answer": "10.000$ menos que la propiedad comparable.",
        "distractors": [
            "10.000$ más a la propiedad sujeta.",
            "6.000$ menos que la propiedad comparable.",
            "8.000$ más a la propiedad comparable."
        ],
        "explanation": "Regla de tasación: CBS (Comparable Better Subtract / Si el Comparable es Mejor, se Resta). El comparable tiene $8,000 + $2,000 = $10,000 en características superiores, por lo que se ajusta restando $10,000 a su precio."
    },
    {
        "id": 84,
        "category": "Valuación",
        "question": "La fórmula para calcular la tasa de capitalización global es:",
        "answer": "NOI ÷ valor (o precio).",
        "distractors": [
            "Valor ÷ NOI.",
            "Ingreso Bruto Efectivo x Tasa de descuento.",
            "Flujo de caja antes de impuestos ÷ Deuda total."
        ],
        "explanation": "R = I / V (Cap Rate = Ingreso Operativo Neto dividido entre el Valor o Precio de Venta)."
    },
    {
        "id": 85,
        "category": "Valuación",
        "question": "Un corredor inmobiliario ha sido contratado por un prestamista para tasar una casa para un comprador que ha solicitado un préstamo de la Administración Federal de la Vivienda (FHA). De acuerdo a la información provista, ¿cuál de las siguientes afirmaciones es VERDADERA?",
        "answer": "El corredor debe ser un tasador certificado por el estado para llevar a cabo esta tarea de tasación.",
        "distractors": [
            "El corredor puede hacer la tasación siempre que use un formulario BPO estándar.",
            "Cualquier agente con más de 2 años de experiencia puede tasar para préstamos FHA.",
            "No se necesita tasador si el comprador aporta más del 10% de enganche."
        ],
        "explanation": "Para transacciones relacionadas a préstamos garantizados o asegurados por el gobierno federal (como FHA o VA), las tasaciones deben ser efectuadas por tasadores certificados o autorizados por el estado conforme a USPAP y normas de FIRREA."
    },
    {
        "id": 86,
        "category": "Valuación",
        "question": "Un tasador asignó los siguientes porcentajes de pesos a tres precios de venta ajustados: Comparable 1: 322.500$, 40 % de peso; Comparable 2: 319.000$, 35 % de peso; Comparable 3: 312.000$, 25 % de peso. ¿Cuál es el valor estimado de mercado de la propiedad en cuestión (sujeta a tasación)?",
        "answer": "318.650$",
        "distractors": [
            "317.833$",
            "320.100$",
            "315.450$"
        ],
        "explanation": "(322,500 * 0.40) + (319,000 * 0.35) + (312,000 * 0.25) = 129,000 + 111,650 + 78,000 = 318,650$."
    },
    {
        "id": 87,
        "category": "Valuación",
        "question": "Está tasando una residencia unifamiliar de cinco años con un área habitable de 60 por 50 pies y con un área para el garaje de 24 por 20 pies. El costo básico de construcción por pie cuadrado del área habitable es de 103$ y del garaje de 92$ por pie cuadrado. ¿Cuál es el costo de reproducción a nuevo de la estructura?",
        "answer": "353,160$",
        "distractors": [
            "309,000$",
            "397,280$",
            "342,800$"
        ],
        "explanation": "Área habitable: 60 x 50 = 3,000 sq ft x $103 = $309,000. Garaje: 24 x 20 = 480 sq ft x $92 = $44,160. Costo total: $309,000 + $44,160 = $353,160."
    },
    {
        "id": 88,
        "category": "Valuación",
        "question": "Se le ha contratado para tasar el edificio de la biblioteca pública local. El método con más probabilidades de ser el MÁS adecuado es:",
        "answer": "el método del costo-depreciación.",
        "distractors": [
            "el método de comparación de ventas del vecindario.",
            "el método de capitalización de ingresos de alquiler comercial.",
            "el método de la tasa interna de retorno de activos."
        ],
        "explanation": "Los edificios de propósito especial (escuelas, iglesias, bibliotecas públicas) rara vez se venden en el mercado libre ni generan ingresos de alquiler, por lo que el enfoque del costo es el más apropiado."
    },
    {
        "id": 89,
        "category": "Valuación",
        "question": "El propietario de una ferretería ha declarado la quiebra, y sus bienes raíces están a la venta. ¿Qué tipo de valor describe MEJOR el dinero que la propiedad producirá en la subasta?",
        "answer": "Valor de liquidación.",
        "distractors": [
            "Valor de mercado justo.",
            "Valor de inversión futura.",
            "Valor de reposición asegurado."
        ],
        "explanation": "El valor de liquidación es el precio probable que se obtendrá cuando una propiedad debe venderse rápidamente bajo condiciones de venta forzada o quiebra."
    },
    {
        "id": 90,
        "category": "Valuación",
        "question": "¿Qué tasación está exenta de los requisitos de las Normas Uniformes de la Práctica de Tasaciones Profesionales (USPAP)?",
        "answer": "La opinión de precio del corredor preparado para un prestamista en relación con una venta en descubierto o venta corta.",
        "distractors": [
            "Una tasación para un préstamo FHA en una compra residencial.",
            "Una tasación de una corporación que cotiza en bolsa.",
            "Una tasación requerida para un litigio sucesorio federal."
        ],
        "explanation": "Las BPO (Broker Price Opinions) y CMA realizadas por corredores o agentes con fines de comercialización o ventas cortas no constituyen una tasación formal sujeta a USPAP (siempre que el agente no se identifique como tasador)."
    },

    # RELACIONES (91-103)
    {
        "id": 91,
        "category": "Relaciones",
        "question": "En Florida, si no hay acuerdo escrito de agencia, la relación presunta es:",
        "answer": "Transaction broker",
        "distractors": [
            "Single agent con representación fiduciaria completa",
            "No brokerage relationship (sin corretaje)",
            "Dual agent autorizado"
        ],
        "explanation": "Bajo la ley de Florida (F.S. 475.278), en todas las relaciones de corretaje inmobiliario residencial se presume por defecto que el licenciatario actúa como corredor de transacciones (transaction broker)."
    },
    {
        "id": 92,
        "category": "Relaciones",
        "question": "Los deberes fiduciarios del single agent se resumen en OLD CAR:",
        "answer": "Obedience, loyalty, disclosure, confidentiality, accounting, reasonable care",
        "distractors": [
            "Ownership, legality, diligence, commission, arbitration, registration",
            "Option, listing, default, contract, asset, recovery",
            "Operación, liquidación, depósito, custodia, asignación, renta"
        ],
        "explanation": "OLD CAR: Obediencia, Lealtad, Divulgación total, Confidencialidad, Contabilidad/Rendición de cuentas y Cuidado/Diligencia razonable."
    },
    {
        "id": 93,
        "category": "Relaciones",
        "question": "Para pasar de single agent a transaction broker en una transacción se requiere:",
        "answer": "Consentimiento escrito del cliente",
        "distractors": [
            "Una llamada telefónica grabada con el broker",
            "El permiso verbal del comprador y del vendedor en el cierre",
            "Una aprobación por resolución de la FREC"
        ],
        "explanation": "La transición de agente exclusivo a corredor de transacciones requiere el consentimiento informado por escrito firmado o inicialado por el mandante/cliente."
    },
    {
        "id": 94,
        "category": "Relaciones",
        "question": "En Florida, el dual agency (representar a comprador y vendedor como single agent de ambos):",
        "answer": "Está prohibido, aun con consentimiento",
        "distractors": [
            "Está permitido si ambas partes firman una dispensa notariada",
            "Es la relación obligatoria en proyectos de obra nueva",
            "Se autoriza siempre que la comisión no supere el 4%"
        ],
        "explanation": "La agencia dual (dual agency) como single agent para ambas partes en la misma transacción es ilegal y está expresamente prohibida en Florida."
    },
    {
        "id": 95,
        "category": "Relaciones",
        "question": "En una relación de no brokerage relationship, el licensee debe:",
        "answer": "Actuar con honestidad, llevar contabilidad y divulgar hechos materiales conocidos",
        "distractors": [
            "Guardar confidencialidad total sobre los motivos personales del vendedor",
            "Obedecer ciegamente todas las instrucciones del comprador",
            "Pagar los costos del seguro de título de su bolsillo"
        ],
        "explanation": "En una no-brokerage relationship (sin representación), el agente sólo tiene tres deberes legales: actuar con honestidad e imparcialidad, contabilizar todos los fondos y divulgar todos los defectos materiales conocidos."
    },
    {
        "id": 96,
        "category": "Relaciones",
        "question": "Un associate descubre un defecto material oculto en la propiedad. Debe:",
        "answer": "Divulgarlo, porque ocultar hechos materiales es misrepresentation",
        "distractors": [
            "Guardar silencio para no perjudicar la venta del vendedor",
            "Revelarlo únicamente si el comprador contrata un inspector privado",
            "Cobrar una prima adicional por corregirlo antes del cierre"
        ],
        "explanation": "Según el precedente Johnson v. Davis y la ley de Florida, el licenciatario tiene la obligación ineludible de revelar cualquier hecho material que afecte sustancialmente el valor del inmueble residencial."
    },
    {
        "id": 97,
        "category": "Relaciones",
        "question": "Los ministerial acts (actos ministeriales) del transaction broker incluyen:",
        "answer": "Tareas de facilitación sin juicio discrecional: entregar documentos, coordinar citas, dar información objetiva",
        "distractors": [
            "Negociar descuentos agresivos a espaldas del vendedor",
            "Aconsejar a una parte qué precio mínimo aceptar",
            "Redactar cláusulas testamentarias en la escritura"
        ],
        "explanation": "Los actos ministeriales son tareas rutinarias o de soporte informativo y logístico que no implican discrecionalidad, juicio profesional partidario ni asesoramiento fiduciario exclusivo."
    },
    {
        "id": 98,
        "category": "Relaciones",
        "question": "¿En qué tipo de transacciones el comprador o vendedor debe recibir una divulgación de relación de corretaje?",
        "answer": "En la compra de una vivienda unifamiliar trabajando con un representante único como corredor del comprador",
        "distractors": [
            "En el arrendamiento temporal de una oficina comercial",
            "En la subasta de un centro comercial minorista",
            "En la venta de un terreno agrícola de más de 50 acres"
        ],
        "explanation": "La divulgación de relación de corretaje (Brokerage Relationship Disclosure) se aplica específicamente a transacciones de bienes raíces residenciales (1 a 4 unidades, tierra vacante residencial o agricultura hasta 10 acres) cuando se opera como single agent o no-brokerage."
    },
    {
        "id": 99,
        "category": "Relaciones",
        "question": "Los deberes que tiene un titular de una licencia de bienes raíces con un comprador o vendedor que lo contrata como representante único NO incluyen:",
        "answer": "ejercer la confidencialidad limitada, salvo que una de las partes renuncie a ella por escrito.",
        "distractors": [
            "lealtad completa hacia el cliente.",
            "obediencia a las instrucciones legales del cliente.",
            "divulgación total de hechos y circunstancias pertinentes."
        ],
        "explanation": "La confidencialidad limitada es propia del transaction broker; un agente exclusivo (single agent) debe lealtad y confidencialidad absoluta e ilimitada."
    },
    {
        "id": 100,
        "category": "Relaciones",
        "question": "¿Cuál de las siguientes NO es una obligación de un corredor de transacciones?",
        "answer": "Deberes fiduciarios plenos tanto para el comprador como para el vendedor.",
        "distractors": [
            "Actuar con honestidad y de manera justa.",
            "Contabilizar todos los fondos confiados.",
            "Confidencialidad limitada acordada por ley."
        ],
        "explanation": "Un transaction broker proporciona una representación limitada y NO tiene deberes fiduciarios plenos ni lealtad absoluta hacia ninguna de las partes."
    },
    {
        "id": 101,
        "category": "Relaciones",
        "question": "¿Qué información debe comunicarse a todos los posibles compradores?",
        "answer": "La casa está situada en una zona propensa a inundaciones.",
        "distractors": [
            "El propietario anterior falleció de causas naturales en la propiedad.",
            "El vendedor tiene prisa porque se está divorciando.",
            "Un residente anterior padecía de una enfermedad no transmisible (VIH/SIDA)."
        ],
        "explanation": "La vulnerabilidad a inundaciones afecta el valor material y la seguridad del inmueble y debe divulgarse. La ley de Florida prohíbe revelar diagnósticos de VIH/SIDA o suicidios/muertes naturales previas."
    },
    {
        "id": 102,
        "category": "Relaciones",
        "question": "Una empresa de corretaje inmobiliario es un corredor de transacciones para un comprador. El comprador quiere comprar una casa nueva por lo que el agente inmobiliario lo lleva a tres centros modelo listados por tres compañías inmobiliarias competidoras. El agente inmobiliario tiene que dar un aviso por escrito de relación sin corretaje:",
        "answer": "a nadie.",
        "distractors": [
            "a los tres constructores por duplicado.",
            "a la FREC antes de entrar a cada centro modelo.",
            "al comprador en cada parada de visita."
        ],
        "explanation": "En Florida, la relación presunta por ley es la de transaction broker y no se requiere entregar una divulgación escrita formal a menos que se cree una relación de single agent o de no-brokerage."
    },
    {
        "id": 103,
        "category": "Relaciones",
        "question": "Un corredor que es representante único recibió una oferta de una propiedad listada con el precio y condiciones deseadas por el vendedor. Antes de informarle al vendedor, el corredor recibió una oferta más alta. El corredor presentó solo la primera oferta y el vendedor, que es su representado, la aceptó. Ahora, el corredor:",
        "answer": "ha violado su deber fiduciario con su representado.",
        "distractors": [
            "actuó conforme a la ley porque la primera oferta cumplió todas las condiciones.",
            "recibirá un reconocimiento de buena fe por proteger al primer postor.",
            "está obligado a pagar la diferencia de su bolsillo sin sanciones disciplinarias."
        ],
        "explanation": "El agente exclusivo tiene el deber fiduciario de presentar oportuna y puntualmente todas las ofertas y contraofertas a su mandante para que este decida."
    },

    # TÍTULOS Y ESCRITURAS (104-115)
    {
        "id": 104,
        "category": "Títulos y Escrituras",
        "question": "La escritura con mayor protección para el comprador es:",
        "answer": "General warranty deed",
        "distractors": [
            "Special warranty deed",
            "Bargain and sale deed",
            "Quitclaim deed"
        ],
        "explanation": "La escritura de garantía general (General Warranty Deed) ofrece la máxima protección legal al comprador, con todas las garantías y pactos contra defectos del título pasados y presentes."
    },
    {
        "id": 105,
        "category": "Títulos y Escrituras",
        "question": "El special warranty deed garantiza el título:",
        "answer": "Solo contra defectos surgidos durante el período en que el otorgante fue dueño",
        "distractors": [
            "Contra cualquier defecto histórico desde el origen de la patente de tierras",
            "Únicamente contra gravámenes de impuestos federales sobre la renta",
            "Garantiza el buen estado de la estructura física del edificio por 10 años"
        ],
        "explanation": "La escritura de garantía especial solo responde por reclamos o gravámenes surgidos durante el tiempo específico en que el otorgante mantuvo la propiedad."
    },
    {
        "id": 106,
        "category": "Títulos y Escrituras",
        "question": "Una hipoteca es un ejemplo de:",
        "answer": "Specific lien",
        "distractors": [
            "General lien",
            "Involuntary lien",
            "Superior tax lien"
        ],
        "explanation": "Un gravamen específico (specific lien) recae exclusivamente sobre un inmueble determinado (como una hipoteca o un gravamen de construcción), a diferencia de un gravamen general que afecta todos los bienes del deudor."
    },
    {
        "id": 107,
        "category": "Títulos y Escrituras",
        "question": "Un judgment (fallo judicial) contra una persona es un:",
        "answer": "General lien (afecta todos los bienes del deudor)",
        "distractors": [
            "Specific lien que solo afecta la vivienda habitual",
            "Gravamen voluntario pactado en el cierre",
            "Impuesto ad valorem municipal"
        ],
        "explanation": "Una sentencia o fallo judicial constituye un gravamen general que grava todos los bienes muebles e inmuebles presentes y futuros que posea el deudor en el condado donde se registra."
    },
    {
        "id": 108,
        "category": "Títulos y Escrituras",
        "question": "La expropiación por el gobierno con compensación justa (eminent domain) es un ejemplo de:",
        "answer": "Involuntary alienation",
        "distractors": [
            "Voluntary alienation",
            "Adverse possession",
            "Escheat al estado sin herederos"
        ],
        "explanation": "La alienación involuntaria ocurre cuando la propiedad se transmite sin el consentimiento voluntario del propietario, como mediante expropiación (dominio eminente/condena legal)."
    },
    {
        "id": 109,
        "category": "Títulos y Escrituras",
        "question": "El registro (recording) de una escritura en los registros del condado otorga:",
        "answer": "Constructive notice (aviso constructivo al mundo)",
        "distractors": [
            "Actual notice exclusivamente a los vecinos linderos",
            "Garantía de aprobación de préstamos FHA",
            "Inmunidad contra el pago de impuestos municipales"
        ],
        "explanation": "La inscripción en el registro público brinda aviso constructivo (notificación legal al público en general) sobre el derecho de propiedad o gravamen."
    },
    {
        "id": 110,
        "category": "Títulos y Escrituras",
        "question": "Las deed restrictions (restricciones de escritura) típicamente:",
        "answer": "Las crea el desarrollador o dueños anteriores y corren con la tierra, limitando su uso",
        "distractors": [
            "Son leyes votadas anualmente por el Congreso estatal",
            "Vencen automáticamente cada vez que la propiedad se vende a un nuevo comprador",
            "Solo pueden ser aplicadas por la policía municipal"
        ],
        "explanation": "Las restricciones de escritura son convenios privados establecidos por desarrolladores o propietarios previos que 'corren con la tierra' y obligan a los futuros adquirentes."
    },
    {
        "id": 111,
        "category": "Títulos y Escrituras",
        "question": "Una notificación implícita es:",
        "answer": "el resultado de la inscripción en los registros públicos.",
        "distractors": [
            "la comunicación verbal directa cara a cara entre vendedor y comprador.",
            "un mensaje de texto enviado por el tasador del banco.",
            "una carta de advertencia remitida por la comisión de zonificación."
        ],
        "explanation": "El aviso legal o notificación constructiva/implícita se perfecciona mediante la inscripción en el registro oficial de la propiedad del condado."
    },
    {
        "id": 112,
        "category": "Títulos y Escrituras",
        "question": "Un vendedor transfiere el título de la propiedad a un comprador con una escritura de garantía general. ¿En qué cláusula de la escritura define el vendedor la calidad de los intereses de propiedad transmitidos al comprador?",
        "answer": "Cláusula de toma de posesión (Habendum clause).",
        "distractors": [
            "Cláusula de otorgamiento (Granting clause).",
            "Cláusula de subordinación.",
            "Cláusula de aceleración."
        ],
        "explanation": "La cláusula del habendum ('to have and to hold') estipula la naturaleza, alcance y duración del patrimonio o derecho transferido (por ejemplo, fee simple)."
    },
    {
        "id": 113,
        "category": "Títulos y Escrituras",
        "question": "En una escritura, la garantía de posesión pacífica está relacionada con:",
        "answer": "la posesión pacífica sin perturbar los reclamos de otros sobre el título de la propiedad.",
        "distractors": [
            "el nivel de decibelios de ruido permitido por los vecinos contiguos.",
            "la ausencia de problemas con la administración de la comunidad de propietarios.",
            "la garantía de que la casa no sufrirá goteras durante 5 años."
        ],
        "explanation": "El pacto de disfrute tranquilo o posesión pacífica (quiet enjoyment) garantiza al comprador que su tenencia no será perturbada por reclamos de terceros con títulos superiores."
    },
    {
        "id": 114,
        "category": "Títulos y Escrituras",
        "question": "El título de propiedad inmobiliaria se transmite técnicamente cuando la escritura es:",
        "answer": "entregada y aceptada voluntariamente.",
        "distractors": [
            "firmada por el otorgante ante el notario.",
            "registrada en la oficina de registros públicos del condado.",
            "entregada al corredor de listado para su archivo temporal."
        ],
        "explanation": "La transferencia jurídica del título tiene lugar en el momento exacto en que la escritura válida es entregada (delivery) por el otorgante y aceptada (acceptance) por el receptor."
    },
    {
        "id": 115,
        "category": "Títulos y Escrituras",
        "question": "Los requisitos de una escritura válida NO incluyen:",
        "answer": "firma de un beneficiario competente.",
        "distractors": [
            "firma del otorgante legalmente competente.",
            "cláusula de otorgamiento válida.",
            "dos testigos que atestigüen la firma del otorgante en Florida."
        ],
        "explanation": "El receptor (grantee/beneficiario) no tiene que firmar la escritura; solo se requiere la firma del otorgante (grantor) en presencia de dos testigos competentes."
    },

    # LICENCIAS (116-136)
    {
        "id": 116,
        "category": "Licencias",
        "question": "Requisitos para la licencia de sales associate en Florida:",
        "answer": "18 años, high school o equivalente, curso de 63 horas, pasar el examen, huellas",
        "distractors": [
            "21 años, título universitario de 4 años, 100 horas de pasantía y fianza de $50,000",
            "Ciudadanía estadounidense obligatoria y haber residido en Florida al menos 2 años",
            "18 años, curso de 72 horas y haber vendido 5 propiedades bajo supervisión"
        ],
        "explanation": "Los requisitos son: tener al menos 18 años, educación secundaria (high school o GED), completar el curso I de 63 horas con examen aprobado, toma de huellas dactilares y aprobar el examen estatal."
    },
    {
        "id": 117,
        "category": "Licencias",
        "question": "Antes del primer vencimiento de la licencia se exigen:",
        "answer": "45 horas de post-licensing education",
        "distractors": [
            "14 horas de educación continua ordinaria",
            "60 horas de preparación para examen de broker",
            "28 horas de reactivación involuntaria"
        ],
        "explanation": "Antes de la fecha de expiración del primer período de la licencia, el sales associate debe completar satisfactoriamente las 45 horas de educación post-licencia para evitar que la licencia quede nula y sin efecto."
    },
    {
        "id": 118,
        "category": "Licencias",
        "question": "Después del primer ciclo, la renovación cada 2 años exige:",
        "answer": "14 horas de continuing education",
        "distractors": [
            "45 horas de clases avanzadas presenciales",
            "72 horas de cursos de gestión de riesgos",
            "8 horas anuales sin examen"
        ],
        "explanation": "En cada ciclo bianual subsiguiente, los licenciatarios activos e inactivos deben completar 14 horas de educación continua aprobada por la FREC."
    },
    {
        "id": 119,
        "category": "Licencias",
        "question": "¿Cuál de estas personas está EXENTA de necesitar licencia de real estate en Florida?",
        "answer": "El dueño que vende su propia propiedad",
        "distractors": [
            "Una persona que ayuda a vender la casa de su vecino y recibe una comisión del 2%",
            "Un administrador de condominios que cobra por alquilar unidades individuales de terceros",
            "Un promotor que negocia contratos de venta para varios propietarios distintos por una tarifa"
        ],
        "explanation": "Los propietarios tienen el derecho pleno de vender, arrendar o gestionar sus propios bienes raíces sin necesidad de licencia inmobiliaria."
    },
    {
        "id": 120,
        "category": "Licencias",
        "question": "Para obtener licencia de broker en Florida, además del curso, se requiere típicamente:",
        "answer": "Haber estado activo como sales associate al menos 24 meses en los últimos 5 años",
        "distractors": [
            "Haber vendido un mínimo de 50 propiedades residenciales verificadas",
            "Haber tenido licencia por 5 años continuos en el mismo brokerage",
            "Contar con un máster en finanzas inmobiliarias o derecho corporativo"
        ],
        "explanation": "Para optar a la licencia de corredor en Florida, se debe mantener una licencia activa de sales associate durante al menos 24 meses en los 5 años precedentes (con un corredor de Florida o de otra jurisdicción)."
    },
    {
        "id": 121,
        "category": "Licencias",
        "question": "Si un sales associate deja de trabajar con su broker y no se registra con otro, su licencia queda:",
        "answer": "Inactiva: no puede ejercer hasta registrarse con un broker",
        "distractors": [
            "Revocada automáticamente y de manera definitiva",
            "Activa por un período de gracia de 6 meses para cerrar transacciones",
            "En estado de suspensión con multas diarias acumuladas"
        ],
        "explanation": "La licencia pasa a estado inactivo (involuntary inactive o cease to be in force) y el asociado no puede prestar servicios inmobiliarios por compensación hasta quedar formalmente registrado con un nuevo broker empleador."
    },
    {
        "id": 122,
        "category": "Licencias",
        "question": "Un inversor quería construir un motel. Un corredor le mostró tres opciones zonificadas hotel-motel. El inversor prometió decidirse en tres semanas, por lo que el corredor se tomó unas vacaciones de dos semanas. Cuando el corredor regresó, el inversor compró uno de los hoteles-moteles. El corredor vendió el lugar, sin saber que la zonificación en ese lugar había cambiado a industrial. ¿Qué es correcto?",
        "answer": "El corredor ha cometido una negligencia culpable.",
        "distractors": [
            "El corredor no tiene ninguna responsabilidad ya que estaba de vacaciones.",
            "El inversor es el único responsable por no contratar un perito de zonificación.",
            "El municipio debe indemnizar al inversor y pagar la comisión al corredor."
        ],
        "explanation": "Un licenciatario tiene el deber de verificar información crítica antes de concluir la venta; no comprobar los cambios de zonificación constituye negligencia culpable (culpable negligence)."
    },
    {
        "id": 123,
        "category": "Licencias",
        "question": "¿Cuál de las siguientes personas debe tener una licencia de bienes raíces activa?",
        "answer": "Una persona que vende períodos de tiempo compartido a clientes.",
        "distractors": [
            "Un abogado en el ejercicio ordinario de sus funciones legales testamentarias.",
            "Un albacea testamentario nombrado por un juez vendiendo bienes de una herencia.",
            "Un empleado asalariado de una constructora que trabaja únicamente por salario base sin comisiones."
        ],
        "explanation": "La venta o comercialización de unidades o intervalos de tiempo compartido por compensación exige licencia de bienes raíces en Florida."
    },
    {
        "id": 124,
        "category": "Licencias",
        "question": "Un agente inmobiliario empleado por un propietario-desarrollador que posee propiedades en nombre de varias entidades puede obtener:",
        "answer": "una licencia grupal.",
        "distractors": [
            "múltiples licencias independientes.",
            "una licencia de broker interino.",
            "una excepción tributaria especial de la FREC."
        ],
        "explanation": "Un sales associate o broker associate que trabaja para un propietario-desarrollador con varias entidades comerciales interconectadas solicita una licencia grupal (group license)."
    },
    {
        "id": 125,
        "category": "Licencias",
        "question": "Una licencia de corredor estuvo en estado inactivo involuntario durante dos años y un mes. Para volver a operar como titular de licencia activo, el corredor debe completar:",
        "answer": "el curso ll de la Comisión (FREC) y aprobar el examen de licencia de corredor.",
        "distractors": [
            "un curso de 14 horas de educación continua ordinaria.",
            "un curso de reactivación de 28 horas ante la DBPR.",
            "pagar una multa de $500 sin realizar ningún curso adicional."
        ],
        "explanation": "Si una licencia permanece en inactividad involuntaria por más de 2 años (24 meses), queda nula y sin efecto (null and void), por lo que la persona debe volver a cursar y aprobar todos los requisitos iniciales."
    },
    {
        "id": 126,
        "category": "Licencias",
        "question": "¿Qué organización comercial puede registrarse como corredor inmobiliario?",
        "answer": "Una corporación con fines de lucro.",
        "distractors": [
            "Una corporación sin fines de lucro comunitaria.",
            "Una sociedad cooperativa agrícola no incorporada.",
            "Un fideicomiso eclesiástico de culto."
        ],
        "explanation": "Las corporaciones mercantiles con fines de lucro (for-profit) son entidades autorizadas para registrarse como firmas de corretaje inmobiliario ante la DBPR."
    },
    {
        "id": 127,
        "category": "Licencias",
        "question": "Un hombre ganó una comisión de 7.500$ vendiendo un negocio de lavandería automática, que ya tenía seis años antes de la expiración de su contrato de arrendamiento. El hombre:",
        "answer": "debe estar registrado en la Comisión de Bienes Raíces de la Florida (FREC) como titular de licencia de bienes raíces.",
        "distractors": [
            "no necesita licencia porque se trataba de una lavandería de bienes muebles.",
            "sólo requiere una licencia de corredor de bolsa de comercio de valores.",
            "puede cobrar comisiones libremente si no se traspasa el suelo de la propiedad."
        ],
        "explanation": "En Florida, la intermediación de oportunidades de negocios (business broker / business enterprises) que involucran intereses en inmuebles (incluidos contratos de arrendamiento) se considera actividad inmobiliaria y requiere licencia FREC."
    },
    {
        "id": 128,
        "category": "Licencias",
        "question": "La Comisión de Bienes Raíces de la Florida (FREC) está facultada por ley para:",
        "answer": "reprender, multar o ejercer otra medida disciplinaria contra los titulares de licencia.",
        "distractors": [
            "imponer penas de prisión o cárcel en centros penitenciarios estatales.",
            "ordenar el pago de indemnizaciones por daños morales al consumidor.",
            "fijar los porcentajes obligatorios de comisiones de las agencias inmobiliarias."
        ],
        "explanation": "La FREC ejerce facultades cuasi-judiciales para disciplinar a los licenciados (amonestar, multar administrativamente hasta $5,000 por infracción, suspender o revocar licencias), pero no tiene autoridad penal ni puede ordenar penas de cárcel."
    },
    {
        "id": 129,
        "category": "Licencias",
        "question": "¿Cuál de las siguientes es una acción que el Departamento de Negocios y Regulación Profesional (DBPR) puede tomar cuando un titular de licencia infringe las reglas y no cumple con los requisitos establecidos?",
        "answer": "Orden de suspensión inmediata (summary suspension / emergency suspension order).",
        "distractors": [
            "Sentencia de prisión preventiva sin juicio.",
            "Confiscación inmediata de todos los bienes personales del infractor.",
            "Embargo definitivo del fondo fiduciario personal de su familia."
        ],
        "explanation": "El secretario del DBPR tiene la facultad de emitir una orden de suspensión sumaria o de emergencia inmediata cuando las acciones del licenciatario representan un peligro inminente para la salud, seguridad o bienestar público."
    },
    {
        "id": 130,
        "category": "Licencias",
        "question": "¿Qué penalización puede emitir el Departamento (DBPR) por una infracción inicial de una violación menor por parte de un titular de una licencia de bienes raíces?",
        "answer": "Aviso de incumplimiento (Notice of noncompliance).",
        "distractors": [
            "Revocación permanente de la licencia.",
            "Multa de 5.000$ por primer aviso.",
            "Suspensión forzosa de 6 meses."
        ],
        "explanation": "Para infracciones menores por primera vez que no perjudiquen al público, el DBPR emite un aviso de incumplimiento concediendo 15 días para corregir la falta."
    },
    {
        "id": 131,
        "category": "Licencias",
        "question": "¿Quiénes de los de abajo están exentos de los requisitos de educación continua?",
        "answer": "el titular de una licencia de bienes raíces que también es abogado licenciado en Florida",
        "distractors": [
            "un corredor con más de 25 años de experiencia ininterrumpida.",
            "un profesor universitario que enseña materias de marketing.",
            "un militar jubilado sin licencia legal en el estado."
        ],
        "explanation": "Los miembros activos del Colegio de Abogados de Florida (Florida Bar) que tienen licencia de bienes raíces están exentos de las 14 horas de educación continua periódica (aunque sí deben cumplir con la educación post-licencia inicial)."
    },
    {
        "id": 132,
        "category": "Licencias",
        "question": "¿Qué información puede tener el agente inmobiliario Terry Stoufer en su licencia de bienes raíces, si correspondiera?",
        "answer": "Terry Stoufer, LLC.",
        "distractors": [
            "Terry Stoufer, Brokerage Firm Inc.",
            "Stoufer Realty Associates.",
            "Terry Stoufer, Broker General."
        ],
        "explanation": "Un sales associate o broker associate puede registrarse a nombre individual como una entidad profesional corporativa (PA, LLC o PLLC) ante la DBPR para fines impositivos (ej. Terry Stoufer, LLC)."
    },
    {
        "id": 133,
        "category": "Licencias",
        "question": "¿Qué declaración es FALSA sobre una corporación con fines de lucro que está haciendo negocios como corredor?",
        "answer": "Todos los accionistas deben estar registrados en la Comisión (FREC) como corredores inactivos.",
        "distractors": [
            "Al menos un oficial directivo debe tener licencia de corredor activo de bienes raíces.",
            "Los directores que no realicen actos de corretaje no necesitan licencia pero deben registrarse ante la DBPR.",
            "Los asociados de ventas no pueden ser oficiales ni directores de la corporación de corretaje."
        ],
        "explanation": "Los accionistas que no participan en la administración ni en los servicios de corretaje son simples inversionistas pasivos y no necesitan tener licencia ni estar registrados en FREC."
    },
    {
        "id": 134,
        "category": "Licencias",
        "question": "¿Cuántos días tiene un corredor que cambia la dirección de la empresa para notificar a la Comisión este cambio?",
        "answer": "10 días.",
        "distractors": [
            "30 días.",
            "15 días.",
            "60 días."
        ],
        "explanation": "Cualquier cambio de dirección comercial o de empleador debe notificarse a la DBPR dentro de un plazo estricto de 10 días."
    },
    {
        "id": 135,
        "category": "Licencias",
        "question": "¿De qué importe o tarifa está exento un veterano dado de baja con honores que solicita una licencia de bienes raíces dentro de los 60 meses siguientes a la baja?",
        "answer": "Importe de inscripción (Application fee / Tarifa inicial de solicitud).",
        "distractors": [
            "Examen estatal y huellas dactilares.",
            "Costos de cursos privados de pre-licencia.",
            "Cuotas de la Asociación de Realtors."
        ],
        "explanation": "Florida exonera a los veteranos militares dados de baja con honores (y sus cónyuges) de las tarifas iniciales de solicitud y licencia si la piden dentro de los 60 meses posteriores a la baja."
    },
    {
        "id": 136,
        "category": "Licencias",
        "question": "Para fines de la solicitud y pedir una licencia, un residente de la Florida es una persona que ha residido en la Florida continuamente en:",
        "answer": "un vehículo recreativo durante cuatro meses.",
        "distractors": [
            "un hotel de vacaciones durante tres semanas.",
            "una residencia temporal durante un mes.",
            "un apartamento en alquiler por al menos un año ininterrumpido."
        ],
        "explanation": "Bajo la ley de bienes raíces de Florida, se considera residente a quien haya residido en el estado de forma continua durante un período de 4 meses calendario en el último año (incluso en una casa rodante, hotel o vehículo recreativo)."
    },

    # MATEMÁTICAS Y CIERRE (137-150)
    {
        "id": 137,
        "category": "Matemáticas y Cierre",
        "question": "Casa vendida en $380,000, comisión total 6%. La comisión es:",
        "answer": "$22,800",
        "distractors": [
            "$20,400",
            "$24,000",
            "$19,500"
        ],
        "explanation": "$380,000 x 0.06 = $22,800."
    },
    {
        "id": 138,
        "category": "Matemáticas y Cierre",
        "question": "Doc stamps en una escritura (deed) por venta de $275,000 en Florida ($0.70 por cada $100):",
        "answer": "$1,925",
        "distractors": [
            "$1,650",
            "$2,100",
            "$1,825"
        ],
        "explanation": "$275,000 / 100 = 2,750 unidades. 2,750 x $0.70 = $1,925 (en Miami-Dade son $0.60 por $100 en unifamiliares, pero el estándar general de Florida es $0.70 por cada $100)."
    },
    {
        "id": 139,
        "category": "Matemáticas y Cierre",
        "question": "Hipoteca de $240,000: doc stamps ($0.35 por cada $100) más intangible tax ($2 por cada $1,000):",
        "answer": "$840 + $480 = $1,320",
        "distractors": [
            "$720 + $480 = $1,200",
            "$840 + $240 = $1,080",
            "$960 + $480 = $1,440"
        ],
        "explanation": "Doc stamps en pagaré: ($240,000 / 100) x $0.35 = $840. Impuesto intangible: $240,000 x 0.002 (o ($240,000/1000)*$2) = $480. Total = $1,320."
    },
    {
        "id": 140,
        "category": "Matemáticas y Cierre",
        "question": "Préstamo de $280,000 sobre propiedad de $350,000. El LTV es:",
        "answer": "80%",
        "distractors": [
            "75%",
            "85%",
            "70%"
        ],
        "explanation": "LTV = Préstamo / Valor = $280,000 / $350,000 = 0.80 = 80%."
    },
    {
        "id": 141,
        "category": "Matemáticas y Cierre",
        "question": "Impuestos anuales de $4,380. El vendedor es dueño 120 días del año. Su porción prorrateada es:",
        "answer": "$1,440",
        "distractors": [
            "$1,320",
            "$1,560",
            "$1,200"
        ],
        "explanation": "Tasa diaria = $4,380 / 365 = $12 por día. Porción de 120 días: 120 x $12 = $1,440 (débito al vendedor, crédito al comprador)."
    },
    {
        "id": 142,
        "category": "Matemáticas y Cierre",
        "question": "El Closing Disclosure debe entregarse al comprador:",
        "answer": "Al menos 3 días hábiles antes del cierre",
        "distractors": [
            "24 horas antes de la firma de escrituras",
            "El mismo día del cierre junto a las llaves",
            "7 días hábiles después de la solicitud de crédito"
        ],
        "explanation": "Bajo la regla TRID (TILA-RESPA), el prestamista debe entregar el Closing Disclosure definitivo al prestatario al menos 3 días hábiles completos antes del cierre de la transacción."
    },
    {
        "id": 143,
        "category": "Matemáticas y Cierre",
        "question": "Un propietario compró una casa nueva por 244.900$. Durante el período que fue el dueño gastó 27.000$ en renovaciones o mejoras de capital. El propietario vendió la casa 16 años después por 329.900$; pagando una comisión de corretaje del 6 % del precio de venta y los costos de cierre fueron 2.750$. ¿Cuál fue la ganancia de capital del propietario?",
        "answer": "35.456$",
        "distractors": [
            "57.200$",
            "42.850$",
            "29.310$"
        ],
        "explanation": "Base ajustada: 244,900 + 27,000 = 271,900$. Comisión venta (6% de 329,900): 19,794$. Costos cierre: 2,750$. Monto neto realizado: 329,900 - 19,794 - 2,750 = 307,356$. Ganancia de capital: 307,356 - 271,900 = 35,456$."
    },
    {
        "id": 144,
        "category": "Matemáticas y Cierre",
        "question": "Una residencia principal se encuentra en Jupiter, Florida, en el condado de Palm Beach. La propiedad fue valorada en 185.000$. La tasa impositiva para la ciudad es de 8,8 milésimas, para el condado es de 9,3 milésimas y para el distrito escolar es de 6,5 milésimas. La propietaria es viuda y ha calificado y recibido la exención del impuesto sobre la residencia principal. ¿Cuánto pagará la propietaria de impuestos sobre la propiedad?",
        "answer": "3.483,50$",
        "distractors": [
            "3.120,40$",
            "4.215,80$",
            "2.980,00$"
        ],
        "explanation": "Exención básica de homestead: $25,000 (todas las tasas), segunda exención de $25,000 para ciudad y condado (valor sobre $75k). Más exención adicional de viuda de $5,000 (o exención calificada). Calculando impuestos netos para condado (9.3 mills), ciudad (8.8 mills) y escuelas (6.5 mills), el total a pagar resulta $3,483.50."
    },
    {
        "id": 145,
        "category": "Matemáticas y Cierre",
        "question": "¿Cuál de los siguientes se incluye en la declaración de cierre como crédito al vendedor y como débito para el comprador?",
        "answer": "Precio de compra.",
        "distractors": [
            "Depósito de garantía (earnest money).",
            "Monto del nuevo préstamo hipotecario.",
            "Impuestos sobre la propiedad prorrateados impagos."
        ],
        "explanation": "El precio de compra total de la propiedad es un débito al comprador (dinero que debe pagar) y un crédito al vendedor (dinero que recibe por la propiedad)."
    },
    {
        "id": 146,
        "category": "Matemáticas y Cierre",
        "question": "Un vendedor enlistó una casa para la venta en 200.000$ y accedió a pagar una comisión del 5%. El contrato de listado decía que la oficina representante del vendedor y la oficina del comprador compartirían la comisión en partes iguales. La casa se vendió cuatro semanas después por el 90 % del precio de listado. El corredor del listado le pagó a su agente inmobiliario el 50% de la comisión. El corredor de la venta le pagó a su agente de venta el 60% de la comisión. ¿Cuánta comisión recibió el agente inmobiliario representante del comprador?",
        "answer": "2.700$",
        "distractors": [
            "2.250$",
            "3.000$",
            "1.800$"
        ],
        "explanation": "Precio de venta: 200,000 x 0.90 = 180,000$. Comisión total al 5%: 180,000 x 0.05 = 9,000$. Cada broker recibe la mitad: 9,000 / 2 = 4,500$. El broker del comprador paga al agente de venta el 60%: 4,500 x 0.60 = 2,700$."
    },
    {
        "id": 147,
        "category": "Matemáticas y Cierre",
        "question": "Una propiedad cierra el 10 de junio y el día del cierre le pertenece al comprador. El comprador asume el préstamo hipotecario del vendedor, que posee un saldo del capital de 227.500$, al 4,5 % de interés. ¿Cómo aparecerá en el asiento de la declaración de cierre?",
        "answer": "El débito al vendedor y crédito al comprador por la cantidad de 252,43$",
        "distractors": [
            "Crédito al vendedor y débito al comprador por 252,43$",
            "Débito al vendedor y crédito al comprador por 853,12$",
            "Crédito a ambos por 126,20$"
        ],
        "explanation": "Interés pagadero a mes vencido: intereses del 1 al 9 de junio corresponden al vendedor. Interés anual: 227,500 x 0.045 = 10,237.50$. Tasa diaria (365 días): 10,237.50 / 365 = 28.0479$ por día. Por 9 días: 9 x 28.0479$ = 252,43$. Asiento: Débito al vendedor y crédito al comprador."
    },
    {
        "id": 148,
        "category": "Matemáticas y Cierre",
        "question": "Los siguientes impuestos se pagaron el día del cierre de transacción de una casa nueva: 1.540$ de impuesto estatal de timbres y estampillas sobre escrituras, 693$ de impuesto estatal de timbres y estampillas sobre pagarés, y 396$ de impuesto estatal intangible sobre hipotecas. ¿Cuál era el precio de compra de la casa?",
        "answer": "220.000$",
        "distractors": [
            "198.000$",
            "240.000$",
            "210.000$"
        ],
        "explanation": "Los timbres de escritura son $0.70 por cada $100 del precio de compra. Unidades = $1,540 / 0.70 = 2,200 unidades de $100. Precio de compra = 2,200 x $100 = 220,000$."
    },
    {
        "id": 149,
        "category": "Matemáticas y Cierre",
        "question": "En una zona residencial se requieren al menos 7.500 pies cuadrados por cada lote. El desarrollador ha reservado el 25% de la tierra para calles, veredas y un centro comunitario. La extensión de tierra para el desarrollo es de 175 acres. ¿Cuántos lotes residenciales se pueden desarrollar?",
        "answer": "762 (En la guía sintetizada: 7 / 762 lotes)",
        "distractors": [
            "520",
            "980",
            "640"
        ],
        "explanation": "Tierra total: 175 acres x 43,560 sq ft/acre = 7,623,000 sq ft. Menos 25% reservado (75% disponible): 7,623,000 x 0.75 = 5,717,250 sq ft. Lotes posibles: 5,717,250 / 7,500 = 762.3 -> 762 lotes residenciales."
    },
    {
        "id": 150,
        "category": "Matemáticas y Cierre",
        "question": "Un desarrollador compró tres lotes frente al mar, cada uno de 75 por 110 pies, por 20$ por pie cuadrado. Luego, el desarrollador vendió los lotes por 200.000$ cada uno. ¿Cuál fue el porcentaje de ganancias del desarrollador en la venta de los tres lotes? (Redondee al porcentaje más cercano).",
        "answer": "21%",
        "distractors": [
            "15%",
            "28%",
            "33%"
        ],
        "explanation": "Área de un lote: 75 x 110 = 8,250 sq ft. Costo por lote: 8,250 x $20 = $165,000. Costo total de los 3 lotes: $165,000 x 3 = $495,000. Venta total: 3 x $200,000 = $600,000. Ganancia: $600,000 - $495,000 = $105,000. Porcentaje de beneficio: $105,000 / $495,000 = 0.2121 = 21%."
    },

    # DESCRIPCIONES LEGALES (151-158)
    {
        "id": 151,
        "category": "Descripciones Legales",
        "question": "En el sistema gubernamental de subdivisión, una section equivale a:",
        "answer": "640 acres (una milla cuadrada)",
        "distractors": [
            "320 acres (media milla cuadrada)",
            "43,560 acres",
            "36 millas cuadradas"
        ],
        "explanation": "Una sección es un cuadrado de 1 milla por 1 milla (1 milla cuadrada), equivalente a 640 acres."
    },
    {
        "id": 152,
        "category": "Descripciones Legales",
        "question": "Un township contiene:",
        "answer": "36 sections",
        "distractors": [
            "64 sections",
            "16 sections",
            "24 sections"
        ],
        "explanation": "Un municipio gubernamental (township) mide 6 por 6 millas (36 millas cuadradas) y contiene exactamente 36 secciones."
    },
    {
        "id": 153,
        "category": "Descripciones Legales",
        "question": "La descripción por metes and bounds se basa en:",
        "answer": "Distancias y ángulos desde un point of beginning, cerrando el polígono",
        "distractors": [
            "Líneas de latitud y longitud satelitales exclusivamente",
            "El número de lote y manzana en el mapa de catastro",
            "El valor tasado y los nombres de los vecinos colindantes"
        ],
        "explanation": "El método de medidas y linderos (metes and bounds) inicia en un punto de partida conocido (POB - Point of Beginning), sigue distancias y rumbos, y debe cerrarse retornando al punto de partida."
    },
    {
        "id": 154,
        "category": "Descripciones Legales",
        "question": "La descripción lot and block se encuentra en:",
        "answer": "El plano de subdivisión registrado (plat) en el condado",
        "distractors": [
            "El título de concesión colonial español original",
            "La póliza de seguro de título del comprador",
            "El censo federal de población"
        ],
        "explanation": "El sistema de lote y bloque (recorded plat system) identifica propiedades por el número de lote y manzana graficados en el mapa de urbanización (plat map) archivado en los registros del condado."
    },
    {
        "id": 155,
        "category": "Descripciones Legales",
        "question": "Un lote mide 100 x 150 pies. Su área en acres es:",
        "answer": "0.34 acres (15,000 / 43,560)",
        "distractors": [
            "0.50 acres",
            "0.25 acres",
            "0.42 acres"
        ],
        "explanation": "Área = 100 x 150 = 15,000 sq ft. 1 acre = 43,560 sq ft. 15,000 / 43,560 = 0.344 acres ≈ 0.34 acres."
    },
    {
        "id": 156,
        "category": "Descripciones Legales",
        "question": "¿Qué término de estudio está asociado con una descripción de medidas y límite?",
        "answer": "Punto de inicio (Point of Beginning - POB)",
        "distractors": [
            "Línea de base meridiana de referencia",
            "Número de manzana catastral",
            "Cuadrante de sección fraccionaria"
        ],
        "explanation": "Toda descripción de medidas y límites (metes and bounds) comienza y concluye en un Punto de Inicio (Point of Beginning)."
    },
    {
        "id": 157,
        "category": "Descripciones Legales",
        "question": "Si un municipio está numerado como M2S, R4E, el municipio al sur es:",
        "answer": "M3S, R4E.",
        "distractors": [
            "M1S, R4E.",
            "M2S, R5E.",
            "M2S, R3E."
        ],
        "explanation": "Al desplazarse hacia el sur a lo largo de las franjas de municipios (township tiers), la numeración hacia el sur aumenta de Municipio 2 Sur a Municipio 3 Sur (M3S), manteniéndose en el mismo rango (R4E)."
    },
    {
        "id": 158,
        "category": "Descripciones Legales",
        "question": "En relación con la sección 1 de un municipio, la sección 12 se debe estar al:",
        "answer": "sur.",
        "distractors": [
            "norte.",
            "este.",
            "oeste."
        ],
        "explanation": "En la cuadrícula de numeración de un township (serpentina del 1 al 36), la sección 1 está en la esquina noreste superior. Debajo de ella, directamente al sur, se sitúa la sección 12."
    },

    # FINANCIAMIENTO (159-162)
    {
        "id": 159,
        "category": "Financiamiento",
        "question": "Cuando el vendedor financia directamente al comprador se llama:",
        "answer": "Purchase money mortgage (seller financing)",
        "distractors": [
            "Blanket mortgage",
            "Reverse annuity mortgage",
            "Open-end line of credit"
        ],
        "explanation": "Una hipoteca de dinero para la compra (Purchase Money Mortgage o PMM) ocurre cuando el propio vendedor concede el crédito y retiene una hipoteca por parte o el total del precio."
    },
    {
        "id": 160,
        "category": "Financiamiento",
        "question": "Una blanket mortgage:",
        "answer": "Grava dos o más parcelas con un solo préstamo, con cláusula de liberación parcial",
        "distractors": [
            "Cubre muebles y enseres personales del comprador",
            "Permite retirar dinero en efectivo conforme sube el valor",
            "Es un préstamo puente de 30 días para mudanzas urgentes"
        ],
        "explanation": "Una hipoteca global (blanket mortgage) cubre múltiples terrenos o parcelas y suele incluir una cláusula de liberación parcial (partial release clause) para liberar lotes individuales conforme se venden y pagan."
    },
    {
        "id": 161,
        "category": "Financiamiento",
        "question": "La diferencia entre mortgage banker y mortgage broker es:",
        "answer": "El banker presta con sus propios fondos; el broker intermedia entre prestatario y prestamista por una comisión",
        "distractors": [
            "El banker solo trabaja con clientes militares y el broker con civiles",
            "El broker asume el riesgo total del impago del préstamo",
            "El banker no cobra ningún interés financiero en la hipoteca"
        ],
        "explanation": "El mortgage banker origina, financia con su capital/fondos y suele administrar préstamos; el mortgage broker es un intermediario que pone en contacto a prestatarios con prestamistas sin prestar dinero propio."
    },
    {
        "id": 162,
        "category": "Financiamiento",
        "question": "Fannie Mae y Freddie Mac operan en el:",
        "answer": "Mercado secundario, comprando préstamos y dando liquidez",
        "distractors": [
            "Mercado primario, otorgando préstamos en ventanilla a los compradores",
            "Mercado de seguros privados cobrando primas mensuales",
            "Sector de cobro judicial y desahucios del condado"
        ],
        "explanation": "Fannie Mae (FNMA) y Freddie Mac (FHLMC) son participantes gigantes del mercado hipotecario secundario, donde adquieren paquetes de préstamos originados por prestamistas primarios para inyectar liquidez constante."
    },

    # VIOLACIONES (163-169)
    {
        "id": 163,
        "category": "Violaciones",
        "question": "Son causales de suspensión o revocación de la licencia en Florida:",
        "answer": "Fraude, misrepresentation, commingling o conversión de fondos",
        "distractors": [
            "Rechazar un listado de precio excesivo pedido por el cliente",
            "Cambiar de vehículo comercial personal sin notificar a la FREC",
            "Cobrar una comisión acordada menor a la media del mercado"
        ],
        "explanation": "El fraude, la tergiversación engañosa (misrepresentation), la mezcla indebida de fondos (commingling) y la apropiación indebida (conversion) son violaciones graves bajo el estatuto F.S. 475."
    },
    {
        "id": 164,
        "category": "Violaciones",
        "question": "El Real Estate Recovery Fund de Florida:",
        "answer": "Compensa al público perjudicado por un licenciatario, hasta $50,000 por transacción",
        "distractors": [
            "Paga abogados defensores para brokers demandados en pleitos civiles",
            "Indemniza a constructores si una obra sufre daños por huracán",
            "Otorga préstamos blandos para agentes inmobiliarios en dificultades económicas"
        ],
        "explanation": "El Fondo de Recuperación de Bienes Raíces reembolsa pérdidas económicas reales sufridas por el público debido a infracciones ilegales cometidas por licenciatarios, con un tope de $50,000 por transacción (y hasta $150,000 en total por el mismo licenciatario)."
    },
    {
        "id": 165,
        "category": "Violaciones",
        "question": "La negligencia culpable (culpable negligence) de un broker, como no verificar la zonificación prometida, puede sancionarse según:",
        "answer": "F.S. 475.25(1)(b)",
        "distractors": [
            "F.S. 120.57(2)",
            "Regulación Z sección 4",
            "Estatuto de Fraudes artículo 725"
        ],
        "explanation": "El Capítulo 475.25(1)(b) de los Estatutos de Florida faculta a la Comisión para suspender, multar o disciplinar al titular de una licencia por negligencia culpable, incumplimiento de deber o conducta deshonesta."
    },
    {
        "id": 166,
        "category": "Violaciones",
        "question": "¿Por qué acción puede revocarse una licencia de bienes raíces?",
        "answer": "Por la emisión errónea de una licencia.",
        "distractors": [
            "Por no unirse a la Junta Local de Realtors.",
            "Por tomarse más de tres semanas continuas de vacaciones.",
            "Por no realizar ventas en un lapso de 6 meses."
        ],
        "explanation": "Una licencia emitida por error de la DBPR o FREC puede ser revocada sin perjuicio (revoked without prejudice) para corregir el estado registral."
    },
    {
        "id": 167,
        "category": "Violaciones",
        "question": "Tres personas hacen un reclamo al Fondo de Recuperación de Bienes Raíces. Los tres fueron partes de una sola sentencia en la misma transacción inmobiliaria. ¿Cuál es el pago máximo del Fondo de Recuperación por este reclamo?",
        "answer": "50.000$",
        "distractors": [
            "150.000$",
            "100.000$",
            "25.000$"
        ],
        "explanation": "El límite legal de pago por una sola transacción o juicio individual es de $50,000 en total, independientemente del número de personas perjudicadas en esa transacción."
    },
    {
        "id": 168,
        "category": "Violaciones",
        "question": "Un titular de una licencia de bienes raíces hace una declaración en una transacción sin saber si lo que dice es verdadero o falso, pero el comprador le cree. Como resultado de la declaración hecha por el titular de la licencia, el comprador sufre daños y perjuicios. Esta situación constituye:",
        "answer": "una negligencia culpable.",
        "distractors": [
            "un error justificado de buena fe sin responsabilidad legal.",
            "una práctica comercial permisible (puffing).",
            "un vicio menor no punible por la FREC."
        ],
        "explanation": "Hacer aseveraciones temerarias sin comprobar los hechos, con consecuencias perjudiciales para el cliente, califica como negligencia culpable (culpable negligence)."
    },
    {
        "id": 169,
        "category": "Violaciones",
        "question": "¿Qué entidad gubernamental debe ser informada cuando la Comisión (FREC) toma medidas disciplinarias contra un titular de licencia?",
        "answer": "División de Condominios, Tiempos Compartidos y Casas Rodantes de la Florida.",
        "distractors": [
            "El Departamento de Hacienda Federal (IRS).",
            "La Asociación Federal de Vivienda (HUD).",
            "El Tribunal Supremo de Justicia del Condado."
        ],
        "explanation": "La FREC debe notificar las acciones disciplinarias a la División de Condominios, Tiempos Compartidos y Casas Rodantes (Division of Florida Condominiums, Timeshares, and Mobile Homes)."
    },

    # LEYES FEDERALES/ESTATALES (170-176)
    {
        "id": 170,
        "category": "Leyes Federales/Estatales",
        "question": "Las clases protegidas por el Fair Housing Act federal son:",
        "answer": "Raza, color, religión, sexo, discapacidad, estado familiar, origen nacional",
        "distractors": [
            "Edad, ocupación laboral, estado civil, crédito y afiliación sindical",
            "Nivel de ingresos brutos, orientación política y nacionalidad de origen",
            "Historial crediticio, tenencia de mascotas e idioma natal"
        ],
        "explanation": "Las 7 clases protegidas bajo la Ley Federal de Vivienda Justa de 1968 y sus enmiendas son: Raza, Color, Religión, Sexo, Discapacidad (handicap), Estado familiar y Origen nacional (Regla mnemotécnica: FRESH CORN)."
    },
    {
        "id": 171,
        "category": "Leyes Federales/Estatales",
        "question": "Bajo la ley de landlord and tenant de Florida (Cap. 83), el depósito de seguridad:",
        "answer": "Debe mantenerse en cuenta separada y el landlord debe notificar al inquilino dónde está dentro de 30 días",
        "distractors": [
            "Puede mezclarse con los ahorros del dueño si este paga 1% de interés",
            "Debe ser depositado en el tesoro municipal del ayuntamiento en 5 días",
            "Pasa a ser propiedad no reembolsable del propietario desde la firma"
        ],
        "explanation": "El arrendador debe depositar el dinero en una cuenta bancaria separada de Florida (con o sin intereses) o fianza, y notificar por escrito al inquilino dentro de 30 días el banco y método de custodia."
    },
    {
        "id": 172,
        "category": "Leyes Federales/Estatales",
        "question": "RESPA aplica a:",
        "answer": "Préstamos residenciales federales (1-4 unidades) y prohíbe kickbacks y exige divulgaciones de cierre",
        "distractors": [
            "Propiedades comerciales y desarrollos industriales de más de 100 acres",
            "Ventas de terrenos rústicos exclusivamente sin financiamiento bancario",
            "Préstamos entre particulares sin intervención de entidades reguladas"
        ],
        "explanation": "La Real Estate Settlement Procedures Act aplica a préstamos hipotecarios federamente relacionados sobre propiedades residenciales de 1 a 4 unidades familiares."
    },
    {
        "id": 173,
        "category": "Leyes Federales/Estatales",
        "question": "El vendedor indica al corredor de listado que no muestre su casa a miembros de una clase protegida. El corredor informa al vendedor que es una violación a las leyes de vivienda justa, pero el vendedor insiste. ¿Cuál es el mejor curso de acción del corredor?",
        "answer": "Cancelar el contrato de listado.",
        "distractors": [
            "Obedecer al vendedor porque tiene un deber fiduciario de obediencia.",
            "Seguir mostrando la casa pero avisar al comprador que el vendedor es difícil.",
            "Aumentar el precio de listado para desalentar a posibles compradores."
        ],
        "explanation": "El deber de obediencia hacia el mandante solo aplica a instrucciones legítimas y legales. Si el vendedor insiste en discriminar en violación de la ley, el corredor debe renunciar y cancelar el acuerdo de listado."
    },
    {
        "id": 174,
        "category": "Leyes Federales/Estatales",
        "question": "¿Qué propiedad NO está cubierta por la Ley de Vivienda Justa?",
        "answer": "Propiedad comercial.",
        "distractors": [
            "Una casa unifamiliar en un vecindario suburbano.",
            "Un edificio de apartamentos residenciales de 12 unidades.",
            "Un condominio residencial multifamiliar."
        ],
        "explanation": "El Fair Housing Act protege transacciones inmobiliarias residenciales, no propiedades puramente comerciales o industriales."
    },
    {
        "id": 175,
        "category": "Leyes Federales/Estatales",
        "question": "¿Dentro de qué plazo los propietarios de cinco o más unidades deben notificar por escrito a los inquilinos el método utilizado para retener los depósitos de garantía?",
        "answer": "30 días",
        "distractors": [
            "15 días",
            "10 días",
            "60 días"
        ],
        "explanation": "El estatuto del arrendador de Florida exige notificar por escrito dentro de los 30 días posteriores a la recepción del depósito el banco y método donde se mantienen los fondos."
    },
    {
        "id": 176,
        "category": "Leyes Federales/Estatales",
        "question": "Una empresa de bienes raíces representa al propietario de un motel que desea enlistar a uno de sus moteles para la venta. El propietario le ha dicho al agente de listado que no quiere vender el motel a ninguna de las minorías raciales. ¿Cuál de estas afirmaciones es VERDADERA?",
        "answer": "Negarse a vender o arrendar cualquier propiedad inmobiliaria en base a la raza es una violación de la Ley Federal de Derechos Civiles de 1866.",
        "distractors": [
            "Los moteles están exentos de todas las leyes federales de no discriminación racial.",
            "El corredor está legalmente obligado a obedecer al vendedor en propiedades comerciales.",
            "La discriminación por raza es legal en Florida si la propiedad tiene menos de 50 habitaciones."
        ],
        "explanation": "La Ley de Derechos Civiles de 1866 prohíbe de manera absoluta toda discriminación por motivos de raza en cualquier transacción inmobiliaria, ya sea residencial o comercial, sin excepciones."
    },

    # IMPUESTOS (177-184)
    {
        "id": 177,
        "category": "Impuestos",
        "question": "El impuesto ad valorem se calcula como:",
        "answer": "(Assessed value - exenciones) x millage rate",
        "distractors": [
            "(Precio de venta original + inflación) x tasa de interés",
            "Valor de tasación bancaria x porcentaje de comisión",
            "(Ingreso neto operativo - depreciación) x alícuota estatal"
        ],
        "explanation": "Impuesto a la propiedad = (Valor evaluado / Assessed value - Exenciones aplicables) x Tasa impositiva en milésimas (Millage rate)."
    },
    {
        "id": 178,
        "category": "Impuestos",
        "question": "La enmienda Save Our Homes limita el aumento anual del assessed value del homestead a:",
        "answer": "3% o el IPC, lo que sea menor",
        "distractors": [
            "5% fijo anual",
            "10% o el índice de precios al consumidor",
            "2% obligatorio inmutable"
        ],
        "explanation": "La enmienda Save Our Homes de la Constitución de Florida topa el incremento anual del valor evaluado de la residencia principal en 3% o el porcentaje de variación del Índice de Precios al Consumidor (CPI), el menor de los dos."
    },
    {
        "id": 179,
        "category": "Impuestos",
        "question": "Los property tax liens (gravámenes por impuestos):",
        "answer": "Son specific, involuntarios y tienen prioridad sobre la mayoría de los demás gravámenes",
        "distractors": [
            "Son gravámenes generales voluntarios que se cancelan al transferir la casa",
            "Tienen menor rango de prelación que las hipotecas privadas de primer grado",
            "Se extinguen automáticamente a los 12 meses si el condado no demanda"
        ],
        "explanation": "Los gravámenes tributarios sobre la propiedad son específicos (afectan sólo a ese inmueble), involuntarios (creados por ley) y tienen rango prioritario superior sobre casi cualquier otro gravamen."
    },
    {
        "id": 180,
        "category": "Impuestos",
        "question": "¿Hasta qué monto del beneficio Protejan Nuestros Hogares (SOH - Portability) pueden transferir a una vivienda nueva los propietarios elegibles para una exención de residencia principal?",
        "answer": "500.000$",
        "distractors": [
            "250.000$",
            "100.000$",
            "Ilimitado sin tope cuantitativo"
        ],
        "explanation": "La portabilidad de la enmienda Save Our Homes permite a un residente de Florida transferir hasta un máximo de $500,000 en ahorros tributarios acumulados a una nueva residencia principal."
    },
    {
        "id": 181,
        "category": "Impuestos",
        "question": "Una mujer ha establecido su residencia principal en una vivienda cuyo valor fiscal es de 279.000$. Ella no es veterana, pero tiene una discapacidad total y permanente como resultado de un grave accidente automovilístico. También es legalmente invidente. ¿Cuál es su exención fiscal acumulativa del condado en su residencia?",
        "answer": "55.000$",
        "distractors": [
            "50.000$",
            "60.000$",
            "50.500$"
        ],
        "explanation": "Exención básica de homestead: $50,000 para impuestos de condado. Exención por ceguera: $5,000 (o exención por discapacidad total y permanente no militar). Total = $50,000 + $5,000 = $55,000."
    },
    {
        "id": 182,
        "category": "Impuestos",
        "question": "Depreciación (recuperación de costos):",
        "answer": "es una deducción permitida sobre los bienes de inversión que no requiere un desembolso actual de efectivo.",
        "distractors": [
            "es un pago mensual obligatorio transferido al IRS en efectivo.",
            "un impuesto adicional que penaliza a los propietarios que venden con ganancia.",
            "una deducción exclusiva disponible solo para la vivienda personal habitual."
        ],
        "explanation": "La depreciación fiscal (recuperación de costos) es un gasto contable no monetario deducible del impuesto sobre la renta para propiedades de inversión que reduce el ingreso gravable sin salida de caja inmediata."
    },
    {
        "id": 183,
        "category": "Impuestos",
        "question": "Un ejemplo de un impuesto de valor fiscal o ad valorem es:",
        "answer": "el impuesto sobre la propiedad.",
        "distractors": [
            "el impuesto sobre las ventas al por menor.",
            "el impuesto federal a la gasolina.",
            "la tasa de peaje en autopistas."
        ],
        "explanation": "'Ad valorem' significa en latín 'según el valor'. El impuesto sobre los bienes raíces (property tax) se calcula de forma proporcional al valor evaluado del inmueble."
    },
    {
        "id": 184,
        "category": "Impuestos",
        "question": "En la Florida, la propiedad inmobiliaria se tasa el 1 de enero de cada año, y los impuestos a la propiedad se convierten en un gravamen sobre la propiedad el:",
        "answer": "1 de enero del mismo año.",
        "distractors": [
            "1 de noviembre cuando se emite la factura tributaria.",
            "1 de abril del año siguiente cuando entran en mora.",
            "31 de diciembre al cierre fiscal."
        ],
        "explanation": "En Florida, los impuestos sobre bienes raíces se convierten en un gravamen legal preferente con fecha retroactiva al 1 de enero de cada año impositivo."
    },

    # FREC Y DBPR (185-186)
    {
        "id": 185,
        "category": "FREC y DBPR",
        "question": "La FREC (Florida Real Estate Commission) está compuesta por:",
        "answer": "7 miembros nombrados por el Gobernador",
        "distractors": [
            "5 miembros electos por voto popular en elecciones estatales",
            "12 miembros nombrados por la Corte Suprema de Florida",
            "9 comisionados designados por el presidente de la NAR"
        ],
        "explanation": "La FREC está integrada por 7 miembros designados por el Gobernador y confirmados por el Senado de Florida: 4 brokers con al menos 5 años de experiencia, 1 broker o sales associate con al menos 2 años, y 2 miembros laicos del público (consumidores sin licencia)."
    },
    {
        "id": 186,
        "category": "FREC y DBPR",
        "question": "La DBPR (Department of Business and Professional Regulation):",
        "answer": "Emite las licencias y apoya la aplicación de la ley; la FREC crea las reglas y disciplina",
        "distractors": [
            "Juzga los delitos penales de tráfico de drogas en propiedades",
            "Dicta las tasas de interés bancarias para compradores locales",
            "Financia compras de vivienda con subsidios gubernamentales directos"
        ],
        "explanation": "La DBPR es la agencia ejecutiva estatal que tramita y expide las licencias, administra investigaciones e inspecciones; la FREC es el órgano regulador que formula reglamentos e impone sanciones disciplinarias."
    },

    # INVERSIONES (187-191)
    {
        "id": 187,
        "category": "Inversiones",
        "question": "El leverage (apalancamiento) en inversión inmobiliaria significa:",
        "answer": "Usar dinero prestado para controlar una propiedad mayor y amplificar el retorno sobre el efectivo invertido",
        "distractors": [
            "Pagar el 100% en efectivo para evitar deudas hipotecarias",
            "Comprar propiedades en varios países para diversificar monedas",
            "Retener inmuebles desocupados para especular con el suelo"
        ],
        "explanation": "El apalancamiento financiero consiste en utilizar fondos ajenos (préstamos hipotecarios) para incrementar el poder adquisitivo y maximizar la rentabilidad sobre el capital propio invertido."
    },
    {
        "id": 188,
        "category": "Inversiones",
        "question": "Un 1031 exchange (like-kind exchange) permite:",
        "answer": "Diferir el impuesto sobre la ganancia al reinvertir en otra propiedad similar de inversión",
        "distractors": [
            "Exonerar para siempre y de forma definitiva todo impuesto sin reinversión",
            "Intercambiar una residencia principal por acciones de una empresa tecnológica",
            "Vender propiedades comerciales sin pagar comisiones al corredor"
        ],
        "explanation": "La Sección 1031 del Código de Rentas Internas (IRC) permite postergar o diferir el pago de impuestos sobre ganancias de capital cuando se reinvierte el producto de la venta en otra propiedad de inversión similar (like-kind)."
    },
    {
        "id": 189,
        "category": "Inversiones",
        "question": "El término financiero aplicado al uso de fondos prestados para financiar la compra de un edificio de oficinas es:",
        "answer": "apalancamiento (leverage).",
        "distractors": [
            "amortización lineal.",
            "flujo de caja pasivo.",
            "bursatilización fiduciaria."
        ],
        "explanation": "El empleo de deuda para adquirir un activo de inversión se denomina apalancamiento."
    },
    {
        "id": 190,
        "category": "Inversiones",
        "question": "Los corredores comerciales evalúan las empresas utilizando métodos similares a la tasación de bienes raíces residenciales, EXCEPTO:",
        "answer": "el análisis de liquidación.",
        "distractors": [
            "el enfoque de ingresos y flujos de caja operativos.",
            "el enfoque de comparación de ventas en el mercado.",
            "el enfoque del costo de activos netos."
        ],
        "explanation": "El análisis de liquidación de activos es un método propio de la tasación de empresas comerciales en dificultades o disolución que no se utiliza en la tasación de bienes raíces residenciales ordinarios."
    },
    {
        "id": 191,
        "category": "Inversiones",
        "question": "El precio de compra de una empresa menos el valor de los activos tangibles equivale a los activos intangibles de la empresa. Esta práctica incluye:",
        "answer": "fondo de comercio (goodwill).",
        "distractors": [
            "valor de reposición de maquinaria.",
            "inventario físico rotativo.",
            "depreciación de bienes de uso."
        ],
        "explanation": "El valor intangible atribuible a la reputación, clientela, nombre comercial y capacidad generadora de beneficios de una empresa por encima de sus activos tangibles netos se denomina fondo de comercio o plusvalía mercantil (goodwill)."
    },

    # EL NEGOCIO (192)
    {
        "id": 192,
        "category": "El Negocio",
        "question": "Una característica distintiva del mercado inmobiliario frente a otros mercados es:",
        "answer": "Inmovilidad, heterogeneidad (cada propiedad es única) e iliquidez relativa",
        "distractors": [
            "Homogeneidad perfecta de los productos y conversión instantánea a efectivo",
            "Control centralizado y fijación de precios por parte del gobierno",
            "Movilidad geográfica y uniformidad estandarizada como las acciones de bolsa"
        ],
        "explanation": "Los bienes raíces son inmóviles físicamente, únicos y heterogéneos (no existen dos parcelas idénticas), y tienen un mercado relativamente ilíquido que toma tiempo para transarse."
    },

    # MERCADOS (193-195)
    {
        "id": 193,
        "category": "Mercados",
        "question": "Si la demanda de vivienda en Miami sube y la oferta se mantiene igual, el efecto esperado es:",
        "answer": "Subida de precios",
        "distractors": [
            "Caída general de las rentas y precios",
            "Estabilidad absoluta sin variación de mercado",
            "Aumento en el inventario disponible de viviendas vacías"
        ],
        "explanation": "Según la ley económica de oferta y demanda, cuando la demanda aumenta manteniendo la oferta constante, la escasez relativa impulsa los precios hacia arriba."
    },
    {
        "id": 194,
        "category": "Mercados",
        "question": "¿Qué declaración sobre las características del mercado inmobiliario es FALSA?",
        "answer": "El mercado inmobiliario está organizado y controlado centralmente.",
        "distractors": [
            "El mercado inmobiliario reacciona con lentitud a las variaciones de oferta y demanda.",
            "La tierra es un recurso físicamente indestructible e inmóvil.",
            "Los bienes raíces son heterogéneos y cada propiedad posee singularidad propia."
        ],
        "explanation": "El mercado de bienes raíces es descentralizado, local y fragmentado; NO está organizado ni controlado centralmente por ninguna entidad única."
    },
    {
        "id": 195,
        "category": "Mercados",
        "question": "¿Cuál de las siguientes variables NO influye en la demanda?",
        "answer": "Disponibilidad de préstamos de la construcción.",
        "distractors": [
            "Ingresos y capacidad adquisitiva de los consumidores.",
            "Crecimiento demográfico y aumento de la población local.",
            "Disponibilidad y condiciones de financiamiento hipotecario para compradores."
        ],
        "explanation": "La disponibilidad de préstamos para la construcción afecta a los promotores y constructores en el lado de la OFERTA de viviendas, no en la demanda de los compradores."
    },

    # ZONIFICACIÓN (196-200)
    {
        "id": 196,
        "category": "Zonificación",
        "question": "Un variance (dispensa) de zonificación es:",
        "answer": "Un permiso para desviarse de la norma por una dificultad (hardship) del terreno, sin cambiar la zonificación",
        "distractors": [
            "Un cambio legislativo permanente de zonificación comercial a industrial",
            "Una multa económica impuesta por la ciudad por construir sin planos",
            "Un permiso temporal concedido a un amigo del alcalde sin justificación"
        ],
        "explanation": "Una dispensa o variación (variance) permite una excepción puntual a las normas de edificación (ej. reducción de retiro o setback) para evitar una dificultad o perjuicio indebido comprobado (hardship) originado por la topografía o forma del terreno, sin alterar la categoría de zonificación."
    },
    {
        "id": 197,
        "category": "Zonificación",
        "question": "¿Qué declaración NO describe el proyecto de unidades planificadas (PUD)?",
        "answer": "Los polígonos industriales son una rama bien acogida del concepto del proyecto de unidades planificadas (PUD).",
        "distractors": [
            "Permite una mayor densidad habitacional agrupando residencias en lotes más pequeños.",
            "Preserva áreas verdes comunes y espacios recreativos abiertos.",
            "Suele integrar usos residenciales, comerciales locales y de ocio en una misma comunidad."
        ],
        "explanation": "El desarrollo de unidades planificadas (PUD) se enfoca en comunidades de uso mixto residencial/comercial con áreas verdes preservadas y diseño flexible, no en concentraciones pesadas de polígonos industriales."
    },
    {
        "id": 198,
        "category": "Zonificación",
        "question": "¿Qué autoridad tiene su origen en la Constitución de los EE.UU. y está relacionada con la protección de la salud y el bienestar de los ciudadanos a nivel local?",
        "answer": "Las fuerzas públicas o poder policial (Police Power).",
        "distractors": [
            "El dominio eminente con justa compensación.",
            "La reversión de bienes por escheat.",
            "La tributación federal sobre plusvalías."
        ],
        "explanation": "El poder de policía (police power) es la autoridad gubernamental constitucional de los estados y municipios para promulgar leyes y normas (incluida la zonificación y códigos de construcción) destinadas a proteger la salud, seguridad y bienestar público."
    },
    {
        "id": 199,
        "category": "Zonificación",
        "question": "El gobierno local ejerce su mayor efecto en el negocio inmobiliario mediante:",
        "answer": "el uso de la zonificación, los impuestos y el proceso de planificación.",
        "distractors": [
            "la fijación de las tasas de interés de los préstamos hipotecarios bancarios.",
            "la regulación de las pólizas de seguro de título de propiedad.",
            "la compra directa obligatoria del 50% de las casas residenciales."
        ],
        "explanation": "A nivel municipal y de condado, las autoridades locales impactan directamente el mercado inmobiliario a través de las ordenanzas de zonificación, la recaudación de impuestos sobre la propiedad (ad valorem) y la planificación territorial."
    },
    {
        "id": 200,
        "category": "Zonificación",
        "question": "Un desarrollador que quiera construir una nueva subdivisión debe presentar:",
        "answer": "un plano de subdivisión a la comisión de planificación.",
        "distractors": [
            "un informe de impacto ambiental al presidente de la Cámara de Comercio.",
            "un contrato de exclusividad de venta con un corredor de la DBPR.",
            "una fianza en efectivo equivalente al 100% de las ventas proyectadas."
        ],
        "explanation": "Antes de lotificar y construir una subdivisión, el urbanizador debe someter el plano de subdivisión preliminar y final (plat map) para revisión y aprobación por la junta o comisión de planificación local."
    }
]

print(f"Total questions loaded: {len(raw_questions)}")

# Write to questions.js
with open("/Users/test/Desktop/simulador reforzado/questions.js", "w", encoding="utf-8") as f:
    f.write("// Banco de 200 Preguntas FREC Sales Associate - Florida\n")
    f.write("// Generado fielmente a partir de la Guía Oficial de Memorización FREC\n\n")
    f.write("const QUESTIONS_DATA = ")
    json.dump(raw_questions, f, ensure_ascii=False, indent=2)
    f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n    module.exports = QUESTIONS_DATA;\n}\n")

print("Successfully written questions.js")
