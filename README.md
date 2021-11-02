# Weather-Logger

In this project we will collect data from the Sense HAT’s sensors and log it to a file. Then we will use the PyGal module to display that data as a line graph.




First let’s log the temperature to a file every 5 seconds. We can use the emulator to change the temperature. We can use the temperature slider on the emulator to change the temperature. We should see the temperature reading added to the end of weather.txt every 5 seconds. Remember that the emulator tries to behave like a real Sense HAT so we won’t see exactly the same reading even if we don’t change the emulator. Pygal automatically creates labels for the y axis from the data. Let’s add a title and labels for the x axis. We can number the readings starting from 1. We need to add one to the length of the temperature list so that range will return a list of numbers that goes from 1 up to the length of the list. We can also collect and display weather for different weather conditions. For example, a hot summer’s day where the temperature is over 30 degrees C and a cold winter where the temperature drops below freezing.






![image](https://user-images.githubusercontent.com/87609938/139233598-0ce9d943-f130-4f1a-abbb-e001da4cf0ce.png)






![image](https://user-images.githubusercontent.com/87609938/139233650-9c7952c6-08a4-4491-8946-866a7b71de71.png)








![image](https://user-images.githubusercontent.com/87609938/139233678-bceacef9-fa53-4241-9f7e-48126bac9d99.png)

