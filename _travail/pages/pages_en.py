# English versions of the five plain-language pages
V = '/arc/volumes/'
def pages_en(F, T, L, P):
    return [
dict(slug='modulo', key='modulo', eyebrow='Modulo', title="Modulo explained simply: what it keeps, what it throws away",
 desc="Modulo is the remainder of a division: the hour on a clock, a car odometer that rolls back to zero. What it keeps, what it throws away, and what happens when that remainder is taken for the number.",
 rep="Modulo keeps the remainder of a division and throws away the number of turns. On a clock, 3 p.m. and 3 a.m. land on the same spot: the hand says where you are in the turn, not how many turns have gone by. That is very useful, and it becomes dangerous as soon as the remainder is taken for the whole number.",
 body=[("Modulo is a clock", [
  F+"A clock counts from 1 to 12, then starts again. At 15:00 the hand points to 3. Mathematicians write: 15 modulo 12 equals 3. One turn of 12 has been removed, and what is left over has been kept.",
  F+"The odometer of an old car does the same thing. It has six digits: after 999,999 kilometres it shows 000,000. The car is not new. The counter has made one full turn, and that turn is written nowhere.",
  "So modulo is not a calculation error. It answers one precise question correctly: <em>where are we in the turn?</em> It does not answer the other question: <em>how many turns have we made?</em>"]),
 ("What it keeps, what it throws away", [
  T+"Every whole number can be written in exactly one way as <em>some turns of 9, plus a position</em>. For example 19 = 2 turns of 9, plus 1. And 28 = 3 turns of 9, plus 1. The ARC corpus counts positions from 1 to 9: 18 is one turn, and position 9.",
  T+"10, 19, 28 and 1,000,000 all have the same position: 1. If only the position is kept, these four numbers become the same one. And there is no way back: from \"position 1\", nobody can tell which number you started from.",
  T+"The loss can be measured. Among the first million numbers, 111,112 have position 1. Saying only \"position 1\" therefore leaves 111,112 candidates. Counting information the way engineers do (in bits), the position among nine keeps 3.17 bits out of 19.93: 84% of what the number carried is thrown away."]),
 ("When the position is enough, and when it is not", [
  T+"The position is enough for some questions. A number is divisible by 3 exactly when its position is 3, 6 or 9: the turns are not needed.",
  T+"It is not enough for others. 10 and 19 have the same position: one is even, the other odd. 19 and 28 have the same position: one is prime, the other is not. Whenever the answer depends on the turn, modulo cannot give it."]),
 ("When the remainder was taken for the number", [
  F+"In a computer, a counter has a fixed number of digits. When it is full it rolls back to zero, like the car odometer. If the program believes that zero is the real number, it is wrong.",
  F+"It has happened. In 1987, in the Therac-25 radiotherapy machine, a counter that rolled back to zero on its 256th pass caused a safety check to be skipped, and a patient died of an overdose. In 2015 the authorities required Boeing 787s to be restarted before a counter reached its end, at 248 days. In 1999 and in 2019 GPS receivers believed they were twenty years in the past. <a href=\"/en/topics/boeing-787-248-days/\">The Boeing case, with its calculation.</a>"]),
 ("The ARC reading", [
  L+"The corpus does not blame modulo for calculating badly. It blames what was done with it: taking the position for the number, and forgetting that the turns existed. It dates that gesture to Gauss, in 1801, when 9 was written as 0: the end of the turn confused with emptiness.",
  T+"Keeping the turns is keeping everything. If you write down the position, then the position of the number of turns, and so on, you recover the whole number with nothing lost. 2026 is written 2, 6, 9, 1, because 2 × 729 + 6 × 81 + 9 × 9 + 1 = 2026.",
  L+"\"It is the tool that is judged, not those who used it.\""]),
 ("What this page does not claim", [
  "It does not say that modulo is wrong or should be abandoned. Where losing is the goal, it is in its place: the encryption that protects a password or a payment relies precisely on a way back that has been thrown away.",
  "It does not blame modulo for everything. The Patriot missile of 1991 drifted because of a truncated decimal, not a remainder: that is a different gesture, and the corpus keeps them apart."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/", "Modulo: the full dossier, with its theorems and sources (in French)"), ("/arc/dossiers/Modulo_v2_1.pdf", "Modulo (PDF, in French)"), (V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos", "Volume 3, chapter 14: the formula of chaos (in French)"), ("/arc/dossiers/modulo_chaos_verif.py", "The script that redoes the calculations")],
 vois=["boeing", "papillon", "en:prime-numbers"]),

dict(slug='boeing-787-248-days', key='boeing', eyebrow='Boeing 787', title="Why the Boeing 787 had to be restarted before 248 days",
 desc="In 2015 the US aviation authority required Boeing 787s to be powered off and on again: an internal counter overflowed after 248 days. The fact, the calculation, and the gesture behind it.",
 rep="Because an internal counter, left powered without interruption, reached the end of its room after 248 days and started again from zero. At that moment the units that control the electrical generators went into fail-safe mode, and the aircraft could lose its power. The US authority required the aircraft to be powered off and on again at least every 120 days, and then the software to be corrected.",
 body=[("What is established", [
  F+"Airworthiness Directive AD 2015-09-07 of the US Federal Aviation Administration, effective 1 May 2015, says it: a 787 that has been powered continuously for 248 days can lose all alternating-current electrical power, because of a software counter internal to the generator control units that overflows after 248 days of continuous power.",
  F+"If the four main units were powered up at the same time, they switch together, whatever the phase of flight. The directive mentions a possible loss of control of the aircraft. It requires a power-down at least every 120 days.",
  F+"A second directive, AD 2018-20-15, effective 20 November 2018, requires new software in the aircraft's six units."]),
 ("The calculation, to redo yourself", [
  "A computer counter is like a car odometer: it has a fixed number of digits, and when it is full it rolls back to zero.",
  T+"A counter of 31 binary digits can count up to 2³¹, that is 2,147,483,648. If it counts hundredths of a second, it is full after 21,474,836 seconds. A day lasts 86,400 seconds. So: 21,474,836 ÷ 86,400 = 248.55 days.",
  F+"Honesty about this calculation: neither directive publishes the size of the counter or its unit. The 31-binary-digit counter in hundredths of a second is a deduction, made from the match with the 248 days. What the authority does write, in black and white, is the gesture: a counter that overflows."]),
 ("The same gesture, elsewhere", [
  F+"Therac-25, 1987: in a radiotherapy machine, a one-byte counter rolled back to zero on its 256th pass. At zero, a check was skipped. A patient died of it.",
  F+"GPS, 1999 and 2019: the week number is held on ten binary digits and rolls back to zero every 1,024 weeks, or 19.6 years. A receiver that takes this remainder for the date believes it is twenty years earlier.",
  P+"2038: many systems count seconds since 1 January 1970 on 32 binary digits. The counter reaches its limit on 19 January 2038 at 03:14:07. Any uncorrected system that rolls back will then show 13 December 1901."]),
 ("The ARC reading", [
  L+"Engineers have a name for the defect: \"integer overflow\". They have no name for the gesture underneath it. The corpus names it: <em>taking the remainder for the number</em>. The counter keeps the position in the turn and throws away the turn. It is <a href=\"/en/topics/modulo/\">modulo</a>, wired into the machine.",
  L+"\"In each case, the remedy was to keep more turns\": longer counters, years on four digits, weeks on thirteen binary digits."]),
 ("What this page does not claim", [
  "It does not say that a 787 crashed because of this counter: the directive is a precaution, and the corpus reports no accident of this aircraft linked to this defect.",
  "It does not put everything down to the remainder. The Patriot missile of 1991 drifted by 0.34 seconds because of a truncated decimal: a different gesture, which the corpus treats separately."])],
 links=[("/arc/dossiers/lire/Modulo_v2_1/", "Modulo, part 5: the deaths and the failures, with sources (in French)"), ("/arc/dossiers/Modulo_v2_1.pdf", "Modulo (PDF, in French)"), ("/arc/dossiers/modulo_chaos_verif.py", "The script that redoes the calculations")],
 vois=["modulo", "papillon"]),

dict(slug='khufu-pyramid-pi', key='kheops', eyebrow='Pyramid of Khufu', title="The Great Pyramid of Khufu and π: what the seked really says",
 desc="Does the Great Pyramid hide the number π? Its slope, a seked of 5½ palms, gives exactly 44/7: the calculation, the measurements, and what they cannot settle.",
 rep="The builders of the Great Pyramid did not need to know π. They chose a simple slope, the seked: 5½ palms of run for 7 palms of rise. With that slope, the perimeter of the base is exactly 44/7 times the height, that is twice 22/7, a number very close to 2π. The resemblance to π comes from the slope, not from a secret.",
 body=[("What is established", [
  F+"The Egyptians set the slope of a pyramid by the <em>seked</em>: how far you move back horizontally each time you rise one cubit. A cubit is 7 palms. The seked of the Great Pyramid is 5½ palms.",
  F+"Surveys give a height of about 146.6 metres and a half-base of 115.2 metres. The height divided by the half-base is 1.2726."]),
 ("The calculation, to redo yourself", [
  T+"Rising 7 while moving back 5.5 is a slope of 7 ÷ 5.5 = 14/11 = 1.2727. That is the measured number, to within one ten-thousandth.",
  T+"The perimeter of the base is 8 half-bases. Divided by the height, that gives 8 × 11/14 = 44/7 = 6.2857. And 2π is 6.2832. That is where the \"π pyramid\" comes from: from 22/7, the simple fraction the slope produces all by itself.",
  T+"The figure of the ARC corpus, two circles and a square, folded into a pyramid, gives for its part a slope of 1.2720, the square root of the golden ratio. So three numbers sit within a hair of each other: 1.2720 from the figure, 1.2726 from the measurement, 1.2727 from the seked."]),
 ("What the measurements do not settle", [
  F+"The measured ratio is 0.012% away from 44/7 and 0.053% away from 2π. But Petrie's survey has a margin of error of 0.03% to 0.21%. Both gaps are smaller than that margin: the measurement does not decide.",
  F+"The corpus had first written \"exact agreement\" with the golden ratio. It withdrew that wording in September 2026, for the same reason: the gap lies within the margin of error. The withdrawal is kept, dated, in the Register."]),
 ("The ARC reading", [
  L+"The Great Pyramid does not approximate π: it inscribes a closed ratio, 14/11, which can be built with a cord and palms. The \"π pyramid\" of the books is a consequence of it, not a cause.",
  L+"What the figure adds is that the same slope comes out of a square held between two circles, with no measurement at all. Whether the builders knew it or not, the corpus does not say."]),
 ("What this page does not claim", [
  "It does not say that the Egyptians knew π or the golden ratio. It does not say that a message is hidden in the pyramid. It says three checkable things: the slope is a simple ratio, that ratio gives 44/7, and the measurements are too loose to choose between the explanations."])],
 links=[(V+"v02-la-figure/06-chapitre-5-le-carre-illusion-et-l-origine-geometri", "Volume 2, chapter 5: the folded square and the geometry of the Great Pyramid (in French)"), (V+"v02-la-figure/05-chapitre-4-deux-cercles-et-un-carre-le-double-et-l", "Volume 2, chapter 4: two circles and a square (in French)"), (V+"v03-le-code-et-le-registre/05-chapitre-3-les-gestes-historiques-et-leurs-resolut", "Volume 3, chapter 3: \"Khufu does not decide\" (in French)")],
 vois=["hippase", "en:tsirelson-bound"]),

dict(slug='hippasus-square-root-of-2', key='hippase', eyebrow='Hippasus', title="What did Hippasus really discover? The diagonal of the square and √2",
 desc="Hippasus showed that the diagonal of a square cannot be written as a fraction of its side. A crisis of mathematics, or the wrong question? The doubled-square calculation, and the ARC reading.",
 rep="Hippasus showed that the diagonal of a square cannot be written as a fraction of its side. Tradition made a crisis of it: an \"irrational\" number, a number without reason. The ARC corpus reads something else. The diagonal can be drawn, measured and used perfectly well; what failed was the demand to write it as a ratio of two whole numbers.",
 body=[("What tradition establishes", [
  F+"Around 450 BCE, Hippasus of Metapontum, of the school of Pythagoras, studies the diagonal of a square of side 1. He finds that no fraction, however fine, gives its length exactly: the diagonal and the side have no common measure.",
  F+"Today that length is written √2 = 1.41421356…, with decimals that never end and never repeat. This result is proved, and it remains true."]),
 ("The calculation, to redo with a pencil", [
  T+"Draw a square of side 1, then build a second square on its diagonal. That large square cuts into four triangles, each of area 1/2. Its area is therefore 2: it is exactly double the first.",
  T+"In other words: the diagonal, multiplied by itself, gives 2. Not roughly, exactly. It is the problem Socrates has a young slave solve in Plato's <em>Meno</em>: to double a square, build it on its diagonal.",
  T+"A tail of endless decimals is not always the mark of a mystery. One third is written 0.333… when you count by tens, and simply 0.1 when you count by threes. The tail sometimes comes from the writing, not from the thing."]),
 ("The ARC reading", [
  L+"The Greek word <em>alogos</em>, translated as \"irrational\", names the failure of a demand: to express the diagonal as a ratio of two whole numbers. It does not name a defect of the diagonal, which is constructed, measurable and works.",
  L+"The diagonal is exact as a relation: its square is 2. It is endless only as a quantity written in decimals. The crisis was not in the diagonal, but in the question put to it.",
  L+"The corpus sees there a mould that repeats later, with Stevin, with Gauss, with Riemann: a demand for foundations is put to something that was working, an impossible object is obtained, and it is given the name of the impossibility."]),
 ("What this page does not claim", [
  "It does not dispute the proof: √2 is not a fraction in any way of counting, by tens, by threes or otherwise. The corpus says so itself. What it discusses is the word \"irrational\" and the crisis drawn from it, not the theorem."]),
 ("What would bring this reading down", [
  P+"The corpus holds that every crisis of foundations in the history of mathematics comes from a demand for justification put to a calculation that was working. A crisis born from a calculation that stops working by itself, with no such demand, would refute it."])],
 links=[(V+"v06-l-histoire-de-la-preuve/15-chapitre-12-le-probleme-qui-a-cree-le-probleme-hip", "Volume 6, chapter 12: the problem that created the problem, Hippasus (in French)"), (V+"v06-l-histoire-de-la-preuve/14-chapitre-11-le-pourquoi-indecidable-anthologie-de", "Volume 6, chapter 11: the undecidable why, with the Meno (in French)"), (V+"v02-la-figure/02-chapitre-1-la-figure-fondamentale", "Volume 2, chapter 1: the fundamental figure and √2 (in French)")],
 vois=["kheops", "en:tsirelson-bound", "modulo"]),

dict(slug='butterfly-effect', key='papillon', eyebrow='Butterfly effect', title="Is the butterfly effect in nature or in the calculation?",
 desc="The butterfly effect and chaos theory: where does the divergence in the calculations come from? A truncated measurement, a thrown-away count of turns, and a test you can redo in a few lines.",
 rep="In the calculations where it was discovered, the butterfly effect comes from two gestures of the tool: a measurement cut short at the start, and a count of turns thrown away at each step. When the count of turns is kept, the calculation can be traced back exactly. The ARC corpus concludes that this chaos is manufactured by the calculation. What diverged in 1961 was not the sky: it was three retyped decimals.",
 body=[("What is established", [
  F+"In 1961 the meteorologist Edward Lorenz restarts a simulation by retyping a number with three decimals, 0.506, instead of the six the machine was keeping, 0.506127. The two calculations part completely. He publishes in 1963. From this came the image of the butterfly whose wingbeat would change the weather on the other side of the world.",
  F+"The mechanism is known to mathematicians: a calculation that stretches then folds, and loses at each step a little of what it knew. The corpus does not claim to have discovered it. What it offers is a reading."]),
 ("Two runners on a track", [
  "Imagine two runners on a round track. You take a photo: they are at the same spot. You conclude they are together. But one has run 51 laps and the other 52. The photo shows the position, not the number of laps. That is exactly what a calculation that \"folds\" does.",
  T+"The calculation, to redo: start from 1/5, and from a number very close to it, 1/5 + 1/256. At each step, double the number and keep only what comes after the decimal point. The gap doubles at each step. At the eighth step the two numbers have the same position, 1/5. Their thrown-away turns, added up, come to 51 for one and 52 for the other. No decimal has been cut: everything is in exact fractions."]),
 ("The three formulas of chaos", [
  T+"One single form: the gap after n steps is the starting gap multiplied n times by the same factor. The corpus distinguishes three engines in it, and each is enough by itself.",
  T+"<strong>The truncated seed.</strong> Do it yourself. Write one third as 0.333: a third of a thousandth is missing, almost nothing. Multiply by 1000: you get 333, whereas the true result is 333.333… A third is already missing. Multiply again by 1333: 444 is missing. Two exact multiplications, and the starting error has become huge. Over a hundred steps, multiplying by 3 each time, what is missing from one third written 0.3333 becomes a 44-digit number. That is what happened to Lorenz: his seed was truncated, and the calculation grew it.",
  T+"<strong>The fold.</strong> The measurement is perfect, but at each step the position is kept and the turn is thrown away. These are the two runners.",
  T+"<strong>The machine.</strong> A computer does both at once. It keeps 52 binary digits; doubling asks for one more at each step; at step 53 nothing of the start is left."]),
 ("What happens when the turns are kept", [
  T+"If the thrown-away turn is written down at each step, the starting point is recovered with no error at all, as far back as you like. In the calculations studied, the confusion disappears as soon as the count of turns is kept.",
  F+"Independent check: in 2018 Saito and Yamaguchi simulate this same calculation in exact arithmetic, with no rounding at all. It remains chaotic. The chaos of the fold therefore does not come from rounding: it comes from the thrown-away turn."]),
 ("The ARC reading", [
  L+"\"The butterfly effect is not the beat of a wing: it is the fate of a count of turns that the fold throws away.\" The system was confused with the measurement of the system. What Lorenz saw diverge were numbers handled by a tool that measures, which is legitimate, and then folds while forgetting."]),
 ("What this page does not claim", [
  "It does not say that the weather can be forecast indefinitely. Every measurement is finite, and the corpus holds that limit to be legitimate: that is not what it accuses.",
  "It does not say that Lorenz's equations are wrong. They grow the gap they are given, and they do so exactly. It says that the gap of 1961 was manufactured by the printer, and that with no gap at the start there is nothing to grow."]),
 ("What would bring this reading down", [
  P+"Producing a system in which two different starting points become impossible to tell apart although the operation keeps the count of turns. The corpus states that this does not happen, and gives the test to check it."])],
 links=[(V+"v03-le-code-et-le-registre/18-chapitre-14-la-formule-du-chaos", "Volume 3, chapter 14: the formula of chaos (in French)"), ("/arc/dossiers/lire/Les_trois_corps_n_ont_jamais_bouge/", "The three bodies never moved (in French)"), ("/arc/dossiers/lire/Modulo_v2_1/", "Modulo: formula II of chaos is its gesture (in French)"), ("/arc/dossiers/modulo_chaos_verif.py", "The script that redoes the calculations")],
 vois=["modulo", "boeing", "en:quantum-physics"]),
]
