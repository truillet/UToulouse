# Interaction vocale

## Cours
* [Interaction vocale en entrée et sortie](https://github.com/truillet/ups/blob/master/m2ihm/Cours/I_V(IO)_Master_3_0.pdf) (2025)

### GrXML / SSML
* **[GrXML pour SAPI 5](https://github.com/truillet/ups/blob/master/m2ihm/Cours/GrXML.pdf)**
   * [Spécification grXML](https://www.w3.org/TR/speech-grammar)
* **[support SSML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/Memo/ssml.pdf)**
   * [Speech Synthesis Markup Language - SSML](https://www.w3.org/TR/speech-synthesis11) 

### autres liens "intéressants"
   * [seeing with sound](https://www.seeingwithsound.com/webvoice/webvoice.htm) : un exemple de transmodalité 
   * [Renault 25 et TTS](https://www.dailymotion.com/video/x2vt9b)

## Travaux Pratiques
### TP1 - Intéraction vocale
[Interaction vocale](https://github.com/truillet/ups/blob/master/m2ihm/TP/lab1_vocal.md) (2025)

**Les outils utilisés par le TP** :
  * agent de reconnaissance vocale / Speech Recognizer agent [sra5](https://github.com/truillet/ivy/blob/master/agents/sra5.zip)
  * agent de synthèse vocale / speech Synthesis agent [ppilot5 v 3.3](https://github.com/truillet/ivy/blob/master/agents/ppilot5_3.3.zip)
 * outil de supervision ivy / ivy monitoring tool [Probe](https://github.com/truillet/ivy/blob/master/code/Probe.zip) ou / or [visionneur](https://github.com/truillet/ivy/blob/master/code/visionneur_1_2.zip) 

**Exemples**
* Exemple de grammaire [grXML](https://github.com/truillet/ups/blob/master/m2ihm/Cours/GrXML.pdf) : **[grammar.grxml](https://github.com/truillet/ups/blob/master/m2ihm/TP/grammar.grxml)**
* code Processing permettant l'affichage issu de la reconnaissance vocale et envoi vers la synthèse : **[vocal_ivy](https://github.com/truillet/ups/blob/master/m2ihm/TP/dessert_vocal.zip)**
* code java permettant l'affichage issu de la reconnaissance vocale : **[vocal_ivy.java](https://github.com/truillet/ups/blob/master/m2ihm/TP/vocal_ivy.java)**
* code python utilisant la reconnaissance de parole : **[SR_ivy.py](https://github.com/truillet/tas_de_code/blob/master/Speech_Recognition/SR_ivy.py)**

### TP2 - Multimodalité en sortie
[Multimodalité en sortie](https://github.com/truillet/ups/blob/master/m2ihm/TP/lab2_multimodalite.md) (2025)
  
**Les outils utilisés par le TP** : 
  * agent de synthèse vocale / speech Synthesis agent [ppilot5 v 3.3](https://github.com/truillet/ivy/blob/master/agents/ppilot5_3.3.zip)
  * agent d'affichage braille / braille display agent [Braille_display](https://github.com/truillet/ups/blob/master/m2ihm/TP/Braille_display.zip)
  * [Toulouse.html](https://github.com/truillet/ups/blob/master/m2ihm/TP/Toulouse.html)
 
## Liens
### Reconnaissance de la parole
* [Microsoft Speech Platform](https://docs.microsoft.com/en-us/previous-versions/office/developer/speech-technologies/hh361572(v%3doffice.14))
* [speech recognition for Java/Processing](http://florianschulz.info/stt/)
* [Python speech recognition](https://pypi.org/project/SpeechRecognition/)
* [OpenAI Whisper](https://pypi.org/project/openai-whisper/)

### Synthèse de la parole
* [Un exécutable pour windows](https://github.com/truillet/ups/blob/master/m2ihm/TP/SayStatic.exe)
* [edgeTTS](https://github.com/rany2/edge-tts)
* [MaryTTS]([http://mary.dfki.de](https://github.com/marytts/marytts))  et [py-marytts](https://pypi.org/project/py-marytts/)
* [eSpeak NG TTS](https://github.com/espeak-ng/espeak-ng)
* [coqui-ai](https://github.com/coqui-ai/TTS)
* [Mozilla TTS](https://github.com/mozilla/TTShttps://github.com/mozilla/TTS)
* [MBROLA - Phoneme-to-Speech](https://github.com/numediart/MBROLA)

### Autres liens
* [Support Processing.org](https://github.com/truillet/upssitech/blob/master/SRI/1A/Cours/C_processing.org_2.4.pdf) et liens vers quelques exercices : [TP0](https://github.com/truillet/processing/blob/master/lab0.md), [TP1](https://github.com/truillet/processing/blob/master/lab1.md) et [TP2](https://github.com/truillet/processing/blob/master/lab2.md)
