# Instrucciones para Subir el Repositorio a GitHub

## Paso 1: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. Configura el repositorio:
   - **Repository name**: `prensa-madrid-leximus`
   - **Description**: `Análisis de la música en la prensa diaria madrileña (1849-1939) | Proyecto LexiMus USAL (PID2022-139589NB-C33)`
   - **Visibility**: Public (o Private si lo prefieres)
   - **NO** marques "Initialize this repository with a README" (ya tenemos uno)
   - **NO** añadas .gitignore ni licencia (ya los tenemos)
3. Click en **"Create repository"**

## Paso 2: Conectar el Repositorio Local con GitHub

GitHub te mostrará instrucciones. Usa estas:

```bash
cd /Users/maria/prensa-madrid-leximus

# Añadir el remote (sustituye "tu-usuario" por tu usuario de GitHub)
git remote add origin https://github.com/tu-usuario/prensa-madrid-leximus.git

# O si usas SSH:
git remote add origin git@github.com:tu-usuario/prensa-madrid-leximus.git

# Verificar que el remote se añadió correctamente
git remote -v

# Subir el código
git push -u origin main
```

## Paso 3: Verificar la Subida

Ve a `https://github.com/tu-usuario/prensa-madrid-leximus` y verifica que:
- ✅ README.md se muestra correctamente
- ✅ Estructura de carpetas está completa
- ✅ Todos los archivos están presentes

## Paso 4: Configurar GitHub Pages (Opcional)

Para publicar la visualización web:

1. Ve a **Settings** → **Pages**
2. En **Source**, selecciona:
   - Branch: `main`
   - Folder: `/resultados` (o `/` si prefieres)
3. Click en **Save**
4. GitHub Pages publicará tu sitio en:
   `https://tu-usuario.github.io/prensa-madrid-leximus/resultados/cronologia_periodicos_madrid.html`

## Paso 5: Añadir el Repositorio a la Organización LexiMus (Opcional)

Si quieres que esté en https://github.com/leximususal:

1. Contacta con el administrador de la organización
2. Solicita que te añadan como miembro
3. Transfiere el repositorio:
   - **Settings** → **Danger Zone** → **Transfer ownership**
   - Selecciona: `leximususal`

## Comandos Git Útiles

```bash
# Ver estado del repositorio
git status

# Ver historial de commits
git log --oneline

# Hacer cambios futuros
git add .
git commit -m "Descripción del cambio"
git push

# Actualizar desde GitHub (si otros colaboran)
git pull
```

## Estructura Final del Repositorio

```
prensa-madrid-leximus/
├── .gitignore
├── README.md
├── INSTRUCCIONES_GITHUB.md
├── docs/
│   └── metodologia.md
├── scripts/
│   └── analisis_cronologico_periodicos_madrid.py
└── resultados/
    ├── analisis_cronologico_periodicos_madrid.json
    └── cronologia_periodicos_madrid.html
```

## Siguiente Paso Recomendado

Una vez subido a GitHub, actualiza el README.md con:
- URL real del repositorio
- URL de GitHub Pages (si lo activaste)
- Información de contacto del equipo

---

**¡Listo para publicar!** 🚀
