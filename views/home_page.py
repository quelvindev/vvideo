import flet as ft 
import screeninfo as esif

class HomePage:
    def __init__(self):
        ...
    
    def main(self,page: ft.Page):
        monitor = esif.get_monitors()[0]
        screen_width = monitor.width*0.4
        screen_height = monitor.height*0.3
        page.title = 'Donwload de Vídeos'
        page.window.alignment = ft.alignment.center
        page.window.width = screen_width
        page.window.height = screen_height
        

        #inputs = self.containers(screen_width,screen_height)
        inputs = self.column_one(screen_width,screen_height)
        page.add(inputs)
        page.update()
        

    def containers(self,screen_width,screen_height):

    
        c_input = ft.Container(
            content= ft.TextField(),
            bgcolor= "#D3D3D3",
            width=screen_width*0.8,
            height=screen_height*0.1,
            alignment=ft.alignment.top_left,
            
        )
        c_button = ft.Container(
            content= ft.FilledButton(text="Filled button"),
            bgcolor= "#D3D3D3"
        )

        c_row_bottom = ft.Container(
             ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=40,
                    tooltip="Yep",
                    #on_click=lambda e: page.open(sby),
                ),
                ft.IconButton(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.PINK_700,
                    icon_size=40,
                    tooltip="Nope",
                    #on_click=lambda e: page.open(sbn),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        )

        footer = ft.Row(spacing=0,
                        controls=[]
                        
         
             
        )
        return [footer]
    def column_one(self,screen_width,screen_height):
        def bottom():
            return ft.Row(expand=True,
                          spacing=2,
                          controls=[ 
                                ft.Container(content= ft.TextField(
                                    label="Link",
                                    autofill_hints=ft.AutofillHint.POSTAL_CODE),
                                alignment=ft.alignment.top_left,
                                width=screen_width*0.7,
                                padding=0.5,
                                margin=0.5),
                                ft.Container(content=ft.FilledButton(text="Filled button",width=screen_width*0.2,height=50),
                                             alignment=ft.alignment.top_right,
                                             padding=0.5,
                                             margin=0.5,
                                             width=screen_width*0.2) 
                                ])
            

        def footer():
            return  ft.Row(spacing=2,
                        controls=[
                            
                            ft.Container(
                                content= ft.Text(color="#000000",
                                                 selectable=True, 
                                                 spans=[ft.TextSpan("Processando a informação",
                                                        ft.TextStyle(weight=ft.FontWeight.BOLD),
                                                        ),
                                                        ]
                                                ),
                                bgcolor= "#D3D3D3",
                                
                                padding=0.05,
                                width=screen_width*0.5,
                                height=screen_height*0.1,
                                alignment=ft.alignment.center_left,
                                ),

                            ft.Container(
                                content= ft.Row(
                                    controls=[   
                                        ft.IconButton(
                                        
                                          
                                            tooltip="Nope",
                                            #on_click=lambda e: page.open(sbn),
                                            content=ft.Image(src='img/linkedin.png',
                                                         
                                                             )
                                        ),
                                          ft.IconButton(
                                        
                                            
                                            tooltip="Nope",
                                            #on_click=lambda e: page.open(sbn),
                                            content=ft.Image(src='img/github.png',
                                                             
                                                             )
                                        )
                                        
                                        ],
                                        alignment=ft.alignment.center_right

                                ),
                                bgcolor= "#D3D3D3",
                              
                                
                                width=screen_width*0.45,
                                height=screen_height*0.1,
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

        
        
app_instance = HomePage()

def run(page: ft.Page):
    app_instance.main(page)

ft.app(target=run)