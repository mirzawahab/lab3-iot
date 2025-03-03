print("	ABDUL WAHAB 22-NTU-CS-1337")
#the ssd1306 library you're using does not support the blit() function for drawing custom icons.
#Since blit() is unavailable, we can directly draw pixel-based icons using framebuf.
import machine
import ssd1306
import dht
import time

# Define GPIO pins
DHT_PIN = 4  # DHT11 data pin
SCL_PIN = 9  # I2C Clock
SDA_PIN = 8  # I2C Data

# Initialize DHT11 sensor
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))

# Initialize I2C for OLED display
i2c = machine.SoftI2C(scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Function to draw a simple temperature icon (°C)
def draw_temp_icon(x, y):
    oled.pixel(x, y, 1)
    oled.pixel(x+1, y, 1)
    oled.pixel(x, y+1, 1)
    oled.pixel(x+1, y+1, 1)
    oled.pixel(x+2, y+1, 1)
    oled.pixel(x+3, y+2, 1)

# Function to draw a simple humidity icon (💧)
def draw_humidity_icon(x, y):
    oled.pixel(x, y, 1)
    oled.pixel(x+1, y+1, 1)
    oled.pixel(x+2, y+2, 1)
    oled.pixel(x+1, y+3, 1)
    oled.pixel(x, y+4, 1)

# Main loop
while True:
    try:
        dht_sensor.measure()  # Read sensor values
        time.sleep(2)  # Allow sensor to stabilize
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print("Temperature:", temp, "C | Humidity:", humidity, "%")

        # Clear OLED screen
        oled.fill(0)

        # 🌡️ Temperature Display
        draw_temp_icon(8, 0)  # Draw icon at (0,0)
        oled.text("{}C".format(temp), 10, 0)

        # 💧 Humidity Display
        draw_humidity_icon(8, 16)  # Draw icon at (0,16)
        oled.text("{}%".format(humidity), 10, 16)

        # Display Name
        oled.text("Mirza Wahab", 16, 40)

        oled.show()

    except Exception as e:
        print("Error reading DHT11 sensor:", e)

    time.sleep(2)  # Delay before next reading

