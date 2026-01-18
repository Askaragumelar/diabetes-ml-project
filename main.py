from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# IZINKAN HTML TERHUBUNG KE API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataPasien(BaseModel):
    kehamilan: int
    glukosa: float
    tekanan_darah: float
    ketebalan_kulit: float
    insulin: float
    bmi: float
    riwayat_diabetes: float
    usia: int

@app.post("/prediksi")
def prediksi(data: DataPasien):
    # LOGIKA SEDERHANA DULU (TES)
    if data.glukosa >= 140:
        hasil = "POSITIF DIABETES"
    else:
        hasil = "TIDAK DIABETES"

    return {
        "hasil": hasil
    }