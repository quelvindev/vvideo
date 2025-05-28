import flet as ft 
import screeninfo as esif
from urllib.parse import urlparse
from machine.source_folder import SourceFolder
from social_media.advisor import Advisor



class HomePage:
    def __init__(self,page:ft.Page= None,link= None,):
        self.link = link
        self.page = page
        self.text_info = None
        self.btn_clear = None
        self.advisor = None
        monitor = esif.get_monitors()[0]
        screen_width = monitor.width*0.4
        screen_height = monitor.height*0.3
        page.title = 'Donwload de Vídeos'
        page.window.alignment = ft.alignment.center
        page.window.width = screen_width
        page.window.height = screen_height
        inputs = self.column_one(screen_width,screen_height)
        page.add(inputs)
        page.update()
        
        source = SourceFolder()
        source.mk_folders()
        self.advisor = Advisor()
       


    def is_valid_url(self,url: str) -> bool:
        parsed = urlparse(url)
        return all([parsed.scheme in ('http', 'https','.com'), parsed.netloc])    
        
    def getlink(self,e):
        link = self.link.value.strip()
        print("Link informado:",link )
        is_link = self.is_valid_url(link)
        if is_link:
            self.advisor.lighthouse(link)
            self.text_info.spans = [
                ft.TextSpan(
                        f"Link recebido: {self.link.value}",
                        ft.TextStyle(weight=ft.FontWeight.BOLD, color="#568956"),
                    )
                ]    
        else:
            self.text_info.spans = [
                ft.TextSpan(
                    f"Insira um link válido",
                    ft.TextStyle(weight=ft.FontWeight.BOLD, color="#EE3A3A"),
                )
            ]
            self.link.value = ""
            self.link.border_color ="#EE3A3A"
            self.link.focus()
        self.page.update()
    def getClear(self,e):

        if self.link.value.strip():
            self.link.value = "" 
            self.link.focus()
            self.page.update()
    def copy_pix(self,e):
        
        key = 'b39a79bd-3de3-4f36-8fbe-5dda50038de9'
        self.page.set_clipboard(key),
        self.text_info.spans = [
                ft.TextSpan(
                    f"Chave Pix copiada com sucesso!",
                    ft.TextStyle(weight=ft.FontWeight.BOLD, color="#463AEE"),
                )
            ]
     
        self.page.update()
    def column_one(self,screen_width,screen_height):

        self.link = ft.TextField(   label="Link",
                                    hint_text='Cole o link aqui',
                                    autofill_hints=ft.AutofillHint.URL,
                                    autofocus=True)
        self.text_info = ft.Text(   color="#000000",
                                    selectable=True, 
                                    spans=[ft.TextSpan("Insira o link na caixa de texto!",
                                                        ft.TextStyle(weight=ft.FontWeight.BOLD),
                                                        ),])
        self.btn_clear = ft.IconButton(
                                    icon=ft.Icons.CLEAR,
                                    icon_color="#F7513B",
                                    icon_size=30,
                                    tooltip='Limpar',
                                    alignment=ft.alignment.center,
                                    on_click=self.getClear)
        def bottom():
            return ft.Row(expand=True,
                          spacing=2,
                          alignment=ft.MainAxisAlignment.CENTER,
                          controls=[ 
                                ft.Container(content= 
                                                self.link,
                                                    alignment=ft.alignment.top_left,
                                                    width=screen_width*0.7,
                                                    padding=0.5,
                                                    margin=0.5),
                                ft.Container(content=  
                                                self.btn_clear,
                                                alignment=ft.alignment.top_center,
                                                width=screen_width*0.05,
                                                padding=0.005,
                                                margin=0.005

                                ),
                                ft.Container(content=
                                                ft.FilledButton(
                                                    text="Download",
                                                    width=screen_width*0.2,
                                                    height=50,
                                                    on_click= self.getlink
                                                    ),
                                                    alignment=ft.alignment.top_right,
                                                    padding=0.5,
                                                    margin=0.5,
                                                    width=screen_width*0.2) 
                                ])
            

        def footer():
            return  ft.Row(spacing=2,
                        controls=[
                            
                            ft.Container(
                                content= self.text_info ,
                                bgcolor= "#D3D3D3",
                                
                                padding=0.5,
                                width=screen_width*0.5,
                                height=screen_height*0.1,
                                alignment=ft.alignment.center_left,
                                ),

                            ft.Container(
                                content= ft.Row(
                                            alignment=ft.MainAxisAlignment.END,  # <- alinha todos os itens à direita
                                            expand=True,
                                            controls=[   
                                                ft.IconButton(
                                                    padding = ft.padding.only(2,5,2,5),
                                                    #mouse_cursor = ft.MouseCursor.ZOOM_IN,
                                                    tooltip="Linkedin",
                                                    on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/quelvincarvalho/"),
                                                    content=ft.Image(src='img/linkedin.png')
                                                ),
                                                ft.IconButton(
                                                    padding = ft.padding.only(2,5,2,5),
                                                    tooltip="Github",
                                                    on_click=lambda e: self.page.launch_url("https://github.com/quelvindev"),
                                                    content=ft.Image(src='img/github.png')
                                                ),
                                                 ft.IconButton(
                                                    padding = ft.padding.only(2,5,2,5),
                                                    tooltip="Site",
                                                    on_click=lambda e: self.page.launch_url("https://quelvindev.github.io/meusite/"),
                                                    content=ft.Image(src='img/site.png')
                                                ),
                                                 ft.IconButton(
                                                    padding = ft.padding.only(2,5,2,5),
                                                    tooltip="Doe - Colabore",
                                                    #on_click=lambda e: self.page.set_clipboard("https://github.com/quelvindev"),
                                                    on_click= self.copy_pix,
                                                    content=ft.Image(src='img/doe.png')
                                                )
                                                
                                                ],
                                        

                                                ),
                                            bgcolor= "#D3D3D3",
                                            width=screen_width*0.45,
                                            height=screen_height*0.1,
                                            padding=ft.padding.all(0),
                                            alignment=ft.alignment.center_right,
                                        ),
          


                                ])


        column = ft.Column(
                    expand=True,
                    controls=[
                        bottom(),   
                        ft.Divider( color="#FFFFFF"),
                        footer()
                ]
        )

      
        return column

        
        


def run(page: ft.Page):
    app_instance = HomePage(page)
   
ft.app(target=run)