# Gate Macro (Python)

Bot simples em Python que interage com o menu de um jogo, detectando o “gate” e enviando destinos via teclas. Projeto educacional para demonstrar uso de **PyAutoGUI**, **pyperclip**, **keyboard** e **numpy**.

---

## Funcionalidades

- Detecta automaticamente quando o menu do gate aparece.
- Permite selecionar destinos usando as teclas `1` a `5`.
- Copia o destino para a textbox do jogo e envia automaticamente.
- Tecla `Delete` encerra o script a qualquer momento.

---

## Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install pyautogui pyperclip keyboard numpy
```
Rode o script
```bash
python gate_macro.py
```

Abra o jogo

Quando o menu do gate aparecer, é só pressionar uma das teclas (de 1 a 5) para enviar um destino

Demonstração
![Exemplo do macro](demo.gif)

