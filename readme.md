# Bizneo Bot

Automatización para registrar la jornada laboral en [Bizneo](https://bizneohr.com/) utilizando Python, Selenium y notificaciones del sistema. Permite iniciar sesión automáticamente con credenciales guardadas de forma segura y registrar las horas de trabajo sin intervención manual.

---

## Características

- Inicio de sesión automático en Bizneo vía Microsoft.
- Interacción con la web para registrar las horas de trabajo.
- Notificaciones nativas del sistema operativo para informar sobre el estado del registro.
- Gestión segura de credenciales con `keyring`.
- Interfaz sencilla con `tkinter` para introducir credenciales si no existen.
- Ejecución en segundo plano (`headless` mode).

---

## Requisitos

- Python 3.8 o superior
- Paquetes Python:

```bash
pip install selenium keyring plyer pyinstaller
```

- Driver de Chrome compatible con la versión de Google Chrome instalada.

---

## Instalación

1. Clona este repositorio o descarga el archivo `main.py`.
2. Asegúrate de tener `chromedriver` en el PATH del sistema.
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta el script con Python:

```bash
python main.py
```

---

## Uso

1. La primera vez que se ejecute, aparecerá una ventana para introducir el correo electrónico y la contraseña de Bizneo.
2. Las credenciales se guardarán de forma segura con `keyring`.
3. El bot iniciará sesión automáticamente y registrará la jornada laboral.
4. Recibirás notificaciones del proceso:

- Inicio del registro.
- Éxito del registro.
- Errores técnicos si el registro falla.

---

## Build con PyInstaller

Para generar un ejecutable independiente (`.exe` para Windows), utiliza el siguiente comando:

```
python -m PyInstaller --onefile --windowed --icon=bizneo_bot.ico --hidden-import=plyer.platforms.win.notification bizneo_bot.py
```

- `--onefile`: genera un único ejecutable.
- `--windowed`: evita que aparezca la consola al ejecutar la aplicación.
- `--icon=bizneo_bot.ico`: icono del ejecutable.
- `--hidden-import=plyer.platforms.win.notification`: asegura la correcta importación de notificaciones en Windows.

El ejecutable se generará dentro de la carpeta `dist/`.

---

## Seguridad

- Las credenciales se guardan con `keyring`, evitando exponer contraseñas en texto plano.
- Si se detecta un error de login, las credenciales se pueden eliminar automáticamente para volver a introducirlas.

---

## Limitaciones

- Necesita compatibilidad del `chromedriver` con la versión de Chrome instalada.
- Requiere conexión a Internet activa.
- El bot asume que la interfaz web de Bizneo no cambia significativamente; cambios en los selectores pueden requerir actualizaciones del código.
