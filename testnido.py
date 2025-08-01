import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#pesquisando produto
driver.find_element(By.ID,"search").send_keys("shirt")
driver.find_element(By.ID,"search").send_keys(Keys.ENTER)
print( "Produto Pesquisado 'Shirt' indo para adicionar")
time.sleep(3)

#clicando no produto
driver.find_element(By.XPATH, '//img[@alt="Radiant Tee"]').click()

#clicando em voltar para sair do ad
driver.back()

#clicando no produto novamente
driver.find_element(By.XPATH, '//img[@alt="Radiant Tee"]').click()


#seleciona o tamanho M e cor laranja depois em add to cart
wait.until(EC.element_to_be_clickable((By.ID, "option-label-size-143-item-169"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "option-label-color-93-item-56"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button"))).click()

#aguarda a mensagem de sucesso aparecer
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message-success")))

#clica no ícone do carrinho
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.action.showcart"))).click()

time.sleep(2)

#aguarda o botão "Proceed to Checkout" aparecer dentro do mini-carrinho
wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout"))).click()
print( "Produto (Tamanho M, Laranja) adicionado e checkout iniciado.")



# Aguarda formulário carregar
wait.until(EC.presence_of_element_located((By.NAME, "firstname")))

# Preenche os campos
driver.find_element(By.ID, "customer-email").send_keys("jonathan.thomas@example.com")
driver.find_element(By.NAME, "firstname").send_keys("Jonathan")
driver.find_element(By.NAME, "lastname").send_keys("Thomas")
driver.find_element(By.NAME, "company").send_keys("Minha Empresa")
driver.find_element(By.NAME, "street[0]").send_keys("Rua das Pedras")
driver.find_element(By.NAME, "city").send_keys("Forest Ln")

# Seleciona estado
Select(driver.find_element(By.NAME, "region_id")).select_by_visible_text("California")

# Preenche CEP, país e telefone
driver.find_element(By.NAME, "postcode").send_keys("90001")
Select(driver.find_element(By.NAME, "country_id")).select_by_visible_text("United States")
driver.find_element(By.NAME, "telephone").send_keys("123456789")

# Aguarda a lista de métodos de entrega aparecer
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='ko_unique_1']")))

# Seleciona o  metodo de envio
shipping_radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
shipping_radio.click()

# Clica em "Next"
next_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.continue"))
)
next_button.click()
print("Endereço preenchido e avançando conferencia.")

#Aguarda a página de pagamento carregar
wait.until(EC.url_contains("#payment"))

time.sleep(3)
# Espera o botão estar clicável e clica nele
driver.find_element(By.XPATH,"//button[span[text()='Place Order']]").click()

print("Compra finalizada")
print("Teste Finalizado !")

driver.quit()