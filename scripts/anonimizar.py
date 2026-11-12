import cv2
from PIL import Image
from pathlib import Path

def sanitizar_imagem(caminho_entrada: str, caminho_saida: str) -> None:
    img = cv2.imread(caminho_entrada)
    if img is None:
        print(f"[ERRO] Não foi possível carregar o arquivo: {caminho_entrada}")
        return

    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector_rosto = cv2.CascadeClassifier(cascade_path)
    rostos = detector_rosto.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in rostos:
        regiao_rosto = img[y:y+h, x:x+w]
        rosto_borrado = cv2.GaussianBlur(regiao_rosto, (99, 99), 30)
        img[y:y+h, x:x+w] = rosto_borrado

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img_rgb_final = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_limpa = Image.fromarray(img_rgb_final)
    
    img_limpa.save(caminho_saida, format="WEBP", quality=85, optimize=True)
    print(f"[SUCESSO] Imagem sanitizada salva em: {caminho_saida}")

if __name__ == "__main__":
   
    entrada = "private/fotos-brutas/paciente_exemplo.jpg"
    saida = "assets/evolucao/caso-01.webp"

    Path("assets/evolucao").mkdir(parents=True, exist_ok=True)
    
   