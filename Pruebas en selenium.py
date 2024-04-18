from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def prueba_agregar_tarea(driver):
    # Caso de Prueba 1: Agregar una nueva tarea con título y descripción.
    driver.find_element(By.CSS_SELECTOR, ".example-button-container button").click()  # Abre el modal para agregar una nueva tarea
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")))  # Espera a que aparezca el campo de título
    # Ingresa el título de la tarea
    title_input = driver.find_element(By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")
    title_input.send_keys("Tarea de prueba con título y descripción")
    # Ingresa la descripción de la tarea
    description_input = driver.find_element(By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(3) input")
    description_input.send_keys("Descripción de la tarea de prueba")
    # Agrega la tarea
    driver.find_element(By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)")))  # Espera a que el botón de agregar desaparezca

def prueba_agregar_tarea_sin_descripcion(driver):
    # Caso de Prueba 2: Agregar una nueva tarea sin descripción.
    driver.find_element(By.CSS_SELECTOR, ".example-button-container button").click()  # Abre el modal para agregar una nueva tarea
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")))  # Espera a que aparezca el campo de título
    # Ingresa el título de la tarea
    title_input = driver.find_element(By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")
    title_input.send_keys("Tarea de prueba sin descripción")
    # Agrega la tarea sin descripción
    driver.find_element(By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)")))  # Espera a que el botón de agregar desaparezca

def prueba_verificar_tarea_agregada(driver):
    # Caso de Prueba 3: Verificar que la tarea agregada aparezca correctamente en la lista de tareas.
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".category-header+@mat-card")))  # Espera a que aparezca al menos una tarea
    tasks = driver.find_elements(By.CSS_SELECTOR, ".category-header+@mat-card")
    # Verifica que la última tarea agregada tenga el título correcto
    assert tasks[-1].find_element(By.CSS_SELECTOR, "mat-card-header mat-card-title").text == "Tarea de prueba sin descripción"

def prueba_editar_titulo_tarea(driver):
    # Caso de Prueba 9: Editar el título de una tarea existente.
    # Suponiendo que ya hay tareas existentes en la lista y que deseamos editar la primera tarea.
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".category-header+@mat-card")))  # Espera a que aparezca al menos una tarea
    tasks = driver.find_elements(By.CSS_SELECTOR, ".category-header+@mat-card")
    first_task_title = tasks[0].find_element(By.CSS_SELECTOR, "mat-card-header mat-card-title").text

    # Hacer clic en el botón de editar de la primera tarea
    tasks[0].find_element(By.CSS_SELECTOR, "mat-card-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")))  # Espera a que aparezca el campo de título en el modal de edición

    # Edita el título de la tarea
    title_input = driver.find_element(By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(1) input")
    title_input.clear()  # Limpia el campo de entrada
    title_input.send_keys("Nuevo título para la tarea")

    # Guarda los cambios
    driver.find_element(By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)")))  # Espera a que el botón de guardar desaparezca

    # Verifica que el título de la tarea se haya actualizado correctamente
    updated_task_title = tasks[0].find_element(By.CSS_SELECTOR, "mat-card-header mat-card-title").text
    assert updated_task_title == "Nuevo título para la tarea"

def prueba_editar_descripcion_tarea(driver):
    # Caso de Prueba 10: Editar la descripción de una tarea existente.
    # Hacer clic en el botón de editar de la primera tarea nuevamente
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".category-header+@mat-card")))  # Espera a que aparezca al menos una tarea
    tasks = driver.find_elements(By.CSS_SELECTOR, ".category-header+@mat-card")
    tasks[0].find_element(By.CSS_SELECTOR, "mat-card-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(3) input")))  # Espera a que aparezca el campo de descripción en el modal de edición

    # Edita la descripción de la tarea
    description_input = driver.find_element(By.CSS_SELECTOR, "mat-dialog-content mat-form-field:nth-child(3) input")
    description_input.clear()  # Limpia el campo de entrada
    description_input.send_keys("Nueva descripción para la tarea")

    # Guarda los cambios
    driver.find_element(By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)").click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "mat-dialog-actions button:nth-child(2)")))  # Espera a que el botón de guardar desaparezca

    # Verifica que la descripción de la tarea se haya actualizado correctamente
    updated_task_description = tasks[0].find_element(By.CSS_SELECTOR, "mat-card-content p").text
    assert updated_task_description == "Nueva descripción para la tarea"

def prueba_eliminar_tarea(driver):
    # Caso de Prueba 12: Eliminar una tarea de la lista y verificar que desaparezca correctamente.
    # Guardar la cantidad inicial de tareas
    initial_task_count = len(driver.find_elements(By.CSS_SELECTOR, ".category-header+@mat-card"))

    # Suponiendo que deseamos eliminar la primera tarea de la lista.
    # Hacer clic en el botón de eliminar de la primera tarea
    driver.find_element(By.CSS_SELECTOR, ".category-header+@mat-card mat-card-actions button:nth-child(1)").click()

    # Esperar un segundo para que se elimine la tarea
    time.sleep(1)

    # Verificar que la cantidad de tareas ha disminuido
    current_task_count = len(driver.find_elements(By.CSS_SELECTOR, ".category-header+@mat-card"))
    assert current_task_count == initial_task_count - 1

def ejecutar_pruebas():
    # Configuración del navegador
    driver = webdriver.Chrome()  # Ajusta el path si es necesario
    driver.get("http://localhost:4200/")  # Reemplaza 'url_de_tu_aplicacion' con la URL de tu aplicación

    try:
        prueba_agregar_tarea(driver)
        prueba_agregar_tarea_sin_descripcion(driver)
        prueba_verificar_tarea_agregada(driver)
        prueba_editar_titulo_tarea(driver)
        prueba_editar_descripcion_tarea(driver)
        prueba_eliminar_tarea(driver)

        print("Todas las pruebas se ejecutaron con éxito")

    finally:
        # Cierra el navegador al finalizar las pruebas
        driver.quit()

# Ejecutar todas las pruebas
ejecutar_pruebas()