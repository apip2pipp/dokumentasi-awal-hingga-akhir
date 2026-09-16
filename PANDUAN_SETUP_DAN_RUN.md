# Panduan Setup dan Run Laporan Bangkit

Panduan ini dibuat supaya orang lain atau agent bisa langsung menyiapkan project LaTeX ini, mengedit laporan, lalu membuat PDF final.

## 1. Yang Harus Diinstall

Untuk Windows, install ini dulu:

1. **Git**  
   Download: https://git-scm.com/downloads

2. **Python 3**  
   Download: https://www.python.org/downloads/  
   Saat install, centang **Add Python to PATH**.

3. **MiKTeX**  
   Download: https://miktex.org/download  
   Saat setup, aktifkan pilihan install package otomatis jika diminta.

Opsional tapi disarankan:

- **VS Code** untuk edit file `.tex`.
- Extension VS Code: **LaTeX Workshop**.

## 2. Download Project

### Opsi A: Pakai Git

Buka PowerShell atau Command Prompt, lalu jalankan:

```powershell
git clone https://github.com/apip2pipp/KARYA-TULIS-ILMIAH-LATEX_GEMASTIK-2026.git
cd KARYA-TULIS-ILMIAH-LATEX_GEMASTIK-2026
```

### Opsi B: Download ZIP

1. Buka repository GitHub:
   https://github.com/apip2pipp/KARYA-TULIS-ILMIAH-LATEX_GEMASTIK-2026
2. Klik **Code**.
3. Klik **Download ZIP**.
4. Extract ZIP ke folder kerja.

## 3. Cek Instalasi

Jalankan command ini:

```powershell
python --version
pdflatex -version
bibtex --version
```

Kalau `pdflatex` atau `bibtex` tidak dikenali, restart terminal dulu. Kalau masih gagal, buka MiKTeX Console dan pastikan MiKTeX sudah terinstall benar.

## 4. Cara Build PDF

Masuk ke folder laporan:

```powershell
cd Laporan_Bangkit
```

Lalu build:

```powershell
python build.py
```

Hasil PDF ada di:

```text
Laporan_Bangkit/output/main.pdf
```

## 5. Cara Build Manual Kalau Script Gagal

Jalankan dari folder `Laporan_Bangkit`:

```powershell
pdflatex -interaction=nonstopmode -output-directory=output main.tex
bibtex output/main.aux
pdflatex -interaction=nonstopmode -output-directory=output main.tex
pdflatex -interaction=nonstopmode -output-directory=output main.tex
```

Compile LaTeX memang perlu beberapa kali supaya sitasi dan referensi muncul dengan benar.

## 6. Struktur File Penting

```text
Laporan_Bangkit/
  main.tex                 file utama laporan
  referensi.bib            database referensi BibTeX
  build.py                 script build PDF
  chapters/
    00_abstract.tex
    01_pendahuluan.tex
    02_studi_pustaka.tex
    03_metodologi.tex
    04_hasil_pembahasan.tex
    05_kesimpulan.tex
  images/                  folder gambar laporan
  output/
    main.pdf               hasil PDF setelah build
```

## 7. Bagian Yang Biasanya Diedit

- Judul, penulis, kampus, email: edit di `Laporan_Bangkit/main.tex`.
- Intisari dan Abstract: edit di `Laporan_Bangkit/chapters/00_abstract.tex`.
- Pendahuluan: edit di `Laporan_Bangkit/chapters/01_pendahuluan.tex`.
- Studi pustaka: edit di `Laporan_Bangkit/chapters/02_studi_pustaka.tex`.
- Metodologi: edit di `Laporan_Bangkit/chapters/03_metodologi.tex`.
- Hasil dan pembahasan: edit di `Laporan_Bangkit/chapters/04_hasil_pembahasan.tex`.
- Kesimpulan: edit di `Laporan_Bangkit/chapters/05_kesimpulan.tex`.
- Referensi: edit di `Laporan_Bangkit/referensi.bib`.

## 8. Cara Menambah Gambar

1. Masukkan file gambar ke:

```text
Laporan_Bangkit/images/
```

2. Panggil gambar di file `.tex`, contoh:

```latex
\begin{figure}[htbp]
\centerline{\includegraphics[width=0.8\linewidth]{nama-file-gambar}}
\caption{Keterangan gambar.}
\label{fig:gambar}
\end{figure}
```

Catatan penting: di `main.tex` sekarang `graphicx` masih memakai mode `demo`:

```latex
\usepackage[demo]{graphicx}
```

Mode ini membuat gambar asli tidak muncul dan diganti placeholder. Kalau ingin gambar asli muncul, ubah menjadi:

```latex
\usepackage{graphicx}
```

## 9. Cara Menambah Referensi

Tambahkan data referensi ke:

```text
Laporan_Bangkit/referensi.bib
```

Contoh:

```bibtex
@article{contoh2026,
  author  = {Nama Penulis},
  title   = {Judul Artikel},
  journal = {Nama Jurnal},
  year    = {2026}
}
```

Lalu panggil di teks:

```latex
\cite{contoh2026}
```

Setelah itu rebuild pakai:

```powershell
python build.py
```

## 10. Alternatif Pakai Overleaf

Kalau tidak mau install MiKTeX:

1. Buka https://www.overleaf.com
2. Buat project baru.
3. Upload isi folder `Laporan_Bangkit`.
4. Set `main.tex` sebagai file utama.
5. Compile.

Kalau ada error gambar, cek lagi mode `demo` di `main.tex`.

## 11. Troubleshooting

### `pdflatex` is not recognized

MiKTeX belum masuk PATH atau terminal belum direstart. Restart terminal, lalu cek lagi:

```powershell
pdflatex -version
```

### MiKTeX minta install package

Klik install/yes. Kalau tidak muncul otomatis, buka MiKTeX Console lalu install package yang diminta.

### PDF tidak berubah setelah diedit

Pastikan build dari folder yang benar:

```powershell
cd Laporan_Bangkit
python build.py
```

Lalu buka ulang:

```text
Laporan_Bangkit/output/main.pdf
```

### Referensi muncul tanda tanya `[?]`

Jalankan build lengkap:

```powershell
python build.py
```

Script ini sudah menjalankan `pdflatex`, `bibtex`, lalu `pdflatex` dua kali.

### Gambar tidak muncul

Cek dua hal:

1. File gambar sudah ada di `Laporan_Bangkit/images/`.
2. Ubah `\usepackage[demo]{graphicx}` menjadi `\usepackage{graphicx}` di `main.tex`.

## 12. Instruksi Singkat Untuk Agent

Kalau file ini diberikan ke agent, gunakan instruksi ini:

```text
Kerjakan hanya di folder Laporan_Bangkit kecuali diminta lain.
File utama adalah Laporan_Bangkit/main.tex.
Isi laporan dipisah di Laporan_Bangkit/chapters/.
Jangan ubah file template lomba di Rules-lomba kecuali diminta.
Setelah edit, build dengan:
cd Laporan_Bangkit
python build.py
Verifikasi hasil di Laporan_Bangkit/output/main.pdf.
Jika ada error LaTeX, baca Laporan_Bangkit/output/main.log.
```

## 13. Checklist Sebelum Submit

- PDF berhasil dibuat tanpa error fatal.
- Judul, nama penulis, afiliasi, dan email sudah benar.
- Intisari dan Abstract sudah sesuai template Bangkit Indonesia.
- Kata kunci dan Keywords sudah 5 sampai 6 item.
- Semua gambar punya caption dan label.
- Semua sitasi muncul di daftar pustaka.
- File final yang dikirim adalah `Laporan_Bangkit/output/main.pdf`.
