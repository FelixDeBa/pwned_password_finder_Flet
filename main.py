import flet as ft # type: ignore
import requests
import json
import hashlib
from time import sleep

HEADERS={"user-agent":"Checador de Contraseñas pwneadas v0.1 by Felix"}

def main(page):
    page.title = "Pwned Password Finder"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def test(e):
        page.launch_url('https://haveibeenpwned.com/Passwords')
        
    def buscar_pwd(hashes_json, hash_pwd):
        for hash_json in hashes_json:
            if hash_pwd == hash_json['hash'].lower():
                resultado = {"encontrado":True, "hash":f"{hash_json['hash']}","cuenta":f"{hash_json['cuenta']}"}
                break
            else:
                resultado = {"encontrado":False, "hash":f"{hash_pwd}", "cuenta":"0"}
        
        return resultado
    
    def limpiar_resultados(e):
        resultados.controls=[]
        txt_contra.value=""
        page.update()

    def chk_pwd(e):
        lbl_resultado=ft.Text(
            "",
            color="red",
            #style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
            text_align=ft.TextAlign.LEFT
        )
        btn_revisar.disabled=True
        pr.visible=True
        page.update()
        pwd=txt_contra.value
        if pwd == "":
            resultados.controls=[]
            lbl_resultado.value=f"No se escribio ninguna contraseña"
            lbl_resultado.color="red"
            resultados.controls.append(ft.Card(
            content=ft.Container(
                    content=lbl_resultado,
                    ##border=ft.border.only(bottom=ft.border.BorderSide(1, "black")),
                    )
                )
            )
            btn_revisar.disabled=False
            pr.visible=False
            page.update()
            raise Exception("No se escribio ninguna contraseña")
        

        hash_pwd = hashlib.sha1(pwd.encode()).hexdigest()
        uri=f"https://api.pwnedpasswords.com/range/{hash_pwd[0:5]}"
        consulta=requests.get(uri, headers=HEADERS)
        sleep(2)
        
        if consulta.ok:
            if consulta.text != "":
                hashes_json=[]
                hashes_raw = (consulta.text).split('\r\n')
                for hash_raw in hashes_raw:
                    hashes_json.append({"hash":f"{hash_pwd[0:5]}{hash_raw.split(':')[0]}","cuenta":f"{hash_raw.split(':')[1]}"})
                
                busqueda=buscar_pwd(hashes_json, hash_pwd.lower())
                if busqueda['encontrado']:
                    lbl_resultado.value=f"Password has been cracked at least {busqueda['cuenta']}times."
                    lbl_resultado.color="red"
                else:
                    lbl_resultado.value=f"No se encontro la palabra en bases de datos de Contraseñas crackeadas"
                    lbl_resultado.color="green"
            else:
                lbl_resultado.value=f"La contraseña no aparece en bases de datos de contraseñas crackeadas"
                lbl_resultado.color="green",
        else:
            lbl_resultado.value=f"Error {consulta.status_code} al hacer la consulta, razon {consulta.reason}"
            lbl_resultado.color="red",
        
        resultados.controls=[]
        resultados.controls.append(ft.Card(
            content=ft.Container(
                content=lbl_resultado,
                ##border=ft.border.only(bottom=ft.border.BorderSide(1, "black")),
                
                )
            )
        )
        pr.visible=False
        btn_revisar.disabled=False
        page.update()


    #Input de contraseña
    txt_contra=ft.TextField(label="Contraseña",width=300,password=True,can_reveal_password=True)
    #icono de carga
    pr = ft.ProgressRing(width=16, height=16, stroke_width = 2, visible=False)

    #Botones
    btn_revisar=ft.ElevatedButton(text="Buscar", on_click=chk_pwd)
    btn_limpiar=ft.ElevatedButton(text="Limpiar", on_click=limpiar_resultados)
    filas_btn=ft.Row(
        controls=[
            btn_revisar,
            btn_limpiar,
        ],
        alignment = ft.MainAxisAlignment.CENTER
    )
    filas_input=ft.Row(
        controls=[
            txt_contra,
            pr
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    resultados=ft.Column(
        controls=[],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER, 
        alignment=ft.MainAxisAlignment.CENTER
    )

    columnas=ft.Column(
        controls=[
            filas_input,
            filas_btn,
            resultados,
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,  
    )
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.INFO,
                label="This program uses haveibeenpwned API, see original aplication at \nhttps://haveibeenpwned.com/Passwords \nto learn more",
            ),
        ],
        on_change=test
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        columnas
    )
    page.adaptive = True    
    page.update()
    


ft.app(main)
