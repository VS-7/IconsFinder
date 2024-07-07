import flet as ft

def icon_container(icon):
    return ft.Container(
        padding=ft.padding.all(20),
        bgcolor=ft.colors.WHITE10,
        border_radius=ft.border_radius.all(10),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(name=icon, size=30, color=ft.colors.WHITE),
                ft.Text(value=icon)
            ]    
        ),
        
        height=100,
        width=100,
    )

def main(page: ft.Page):
    
    title = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[ 
            ft.Text(
                value='ICONS FINDER',
                weight=ft.FontWeight.BOLD,
                size=20,
            ),
            ft.Icon(
                ft.icons.EMOJI_OBJECTS_OUTLINED,
                color=ft.colors.WHITE,
                size=30
            ),
            
        
        ]
    )
    
    def search(e):
        value = e.control.value.upper()
        
        icons_grid.controls = []
        for icon in dir(ft.icons):
            if value in icon:
                icons_grid.controls.append(icon_container(icon=icon))
                
        icons_grid.update(),
    
    searchbar = ft.TextField(
        prefix_icon=ft.icons.SEARCH,
        hint_text='Digite algo para buscar...',
        on_submit=search,
        border_radius=ft.border_radius.all(10)
    )
    
    icons_grid = ft.GridView(
        expand=True,
        max_extent=200,
        controls=[],
        child_aspect_ratio=1.0,
    )
    
    layout = ft.Column(
        expand=True,
        controls=[
            title,
            searchbar,
            icons_grid,
        ]
    )
    
    page.add(layout)
    
    
if __name__ == "__main__":
    ft.app(target=main)
