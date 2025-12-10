from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import keyring
import tkinter as tk
from tkinter import messagebox
from plyer import notification

def begin_automation(MAIL_ADDRESS, MAIL_PASSWORD):
    try:
        options = ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--headless") 
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 2
                # with 2 should disable notifications
            },
        )

        driver = webdriver.Chrome(options=options)
        action = webdriver.ActionChains(driver)
        driver.get("https://vantureess.bizneohr.com/")
        assert "Bizneo" in driver.title
        login_button = driver.find_element(By.XPATH, '//a[@href="https://bizneohr.com/sessions/auth/microsoft?prompt=select_account&subdomain=vantureess&zendesk_return_to="]')
        login_button.click()

        time.sleep(3)

        correu_input = driver.find_element(By.ID, "i0116")
        correu_input.clear()
        correu_input.send_keys(MAIL_ADDRESS)
        correu_input.send_keys(Keys.RETURN)

        time.sleep(3)

        password_input = driver.find_element(By.ID, "i0118")
        password_input.clear()
        password_input.send_keys(MAIL_PASSWORD)
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)
        try:
            dont_stay_signed_in_button = driver.find_element(By.ID, "idBtn_Back").click()
        except:
            raise ValueError("Wrong credentials")

        time.sleep(4)

        mis_fichajes_button = driver.find_element(By.XPATH, '//a[@href="/time-attendance/my-logs/17430803"]').click()
        
        time.sleep(2)

        toggle_all_button = driver.find_element(By.CSS_SELECTOR, "th[data-bulk-toggle-all]")
        action.move_to_element(toggle_all_button).perform()
        toggle_all_button.click()

        time.sleep(0.2)

        boton_acciones = driver.find_element(By.CSS_SELECTOR, ".dropdown-btn.no-arrow.button.secondary.mobile-no-text").click()

        time.sleep(0.35)

        menu_desplegable = driver.find_element(By.CLASS_NAME, "tippy-box")

        time.sleep(0.2)

        botones_desplegable = menu_desplegable.find_elements(By.CLASS_NAME, "menu-item")

        for boton in botones_desplegable:
            if "Registrar horario" in boton.get_attribute("innerHTML"):
                boton.click()
                time.sleep(1)
                panel_confirmar = driver.find_element(By.CLASS_NAME, "modal-content")
                boton_confirmar = panel_confirmar.find_element(By.CSS_SELECTOR, ".button.primary")
                boton_confirmar.click()
                break
        time.sleep(5)
        print("Bizneo AL DÍA")

    finally:
        driver.close()

def get_credentials():
    email = keyring.get_password("bizneo_bot", "email")
    password = keyring.get_password("bizneo_bot", "password")

    if not email or not password:
        root = tk.Tk()
        root.title("Introduzca credenciales de bizneo")
        root.geometry("300x150")

        tk.Label(root, text="Email:").pack()
        entry1 = tk.Entry(root)
        entry1.pack()

        tk.Label(root, text="Password:").pack()
        entry2 = tk.Entry(root)
        entry2.pack()
        
        def save_creds():
            keyring.set_password("bizneo_bot", "email", entry1.get())
            keyring.set_password("bizneo_bot", "password", entry2.get())
            root.destroy()

        tk.Button(root, text="Enviar", command=save_creds).pack(pady=10)
        
        root.mainloop()

    email = keyring.get_password("bizneo_bot", "email")
    password = keyring.get_password("bizneo_bot", "password")
    return email, password

def main():
    while True:
        mail, password = get_credentials()
        notification.notify(
            title="El registro de horas esta en proceso",
            message="El registro de horas en Bizneo se está realizando en segundo plano",
            app_name="bizneo_bot",
            timeout=5  # segons que apareix la notificació
        ) 
        try:
            begin_automation(mail, password)
            break
        except ValueError as m:
            print(m)
            keyring.delete_password("bizneo_bot", "email")
            keyring.delete_password("bizneo_bot", "password")
        except:
            notification.notify(
                title="No se pudo registrar Bizneo",
                message="Por motivos técnicos no se pudo registrar la jornada laboral a Bizneo",
                app_name="bizneo_bot",
                timeout=5  # segons que apareix la notificació
            )
            sys.exit()
    
    notification.notify(
        title="Se registró correctamente Bizneo",
        message="El registro de horas en Bizneo fue un éxito",
        app_name="bizneo_bot",
        timeout=5  # segons que apareix la notificació
    )  

if __name__ == "__main__":
    main()