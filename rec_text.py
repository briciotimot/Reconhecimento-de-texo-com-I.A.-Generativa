import cv2
import pytesseract

# Carregar uma imagem
imagem = cv2.imread('imagem_exemplo.png')

# Pré-processamento da imagem (opcional)
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagem_binarizada = cv2.threshold(imagem_gray, 150, 255, cv2.THRESH_BINARY)[1]

# Reconhecimento de texto
texto = pytesseract.image_to_string(imagem_binarizada, lang='por')

# Exibir o resultado
print("Texto reconhecido:")
print(texto)
