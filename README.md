
    ### Para gerar o executável 
    1- Instale pyinstaller

    ```
    pip install pyinstaller
    ```
    2 - Gere o exe

    ```
    pyinstaller --onefile --noconsole --add-data "img;img" --icon=icone.ico app.py

    ```