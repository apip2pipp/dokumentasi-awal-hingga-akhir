# LaTeX Update Progress AuditChain Gateway September 2026

Template ini dibuat supaya laporan update PDF dapat langsung di-build dan diedit per bab.

## Struktur

- `main.tex` - file utama dokumen.
- `chapters/` - isi laporan per bab.
- `images/` - tempat screenshot atau diagram.
- `output/` - hasil build PDF.
- `update-md/` - catatan markdown tambahan.
- `build.bat` - script build Windows.
- `build.py` - script build Python.

## Cara Build

Dari folder ini, jalankan:

```bat
build.bat
```

Atau:

```bash
python build.py
```

Build menggunakan `xelatex` supaya font `Times New Roman` dari Windows dapat dipakai langsung.

PDF final akan dibuat di:

```text
output/Progress_AuditChain_Gateway_September_2026_Lengkap_Update.pdf
```

## Mengganti Placeholder Gambar

Letakkan gambar di folder `images/`, lalu ganti blok:

```tex
\placeholderimage{Judul}{Catatan}
```

menjadi:

```tex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{images/nama-file.png}
    \caption{Judul gambar}
\end{figure}
```
