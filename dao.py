# -*- coding: utf-8 -*-
import sqlite3 as sql
import pandas as pd
import tkinter
import os
import platform
import datetime
import fpdf
from tkinter import messagebox
from database import Data

db = Data()

class Dao:
    def create_table(self):
        try:
            table_sql = 'CREATE TABLE IF NOT EXISTS tb_pedidos (ID INTEGER NOT NULL PRIMARY KEY, Data_Cadastro TEXT, Assistido TEXT, Necessidade TEXT, Idade TEXT, Data_Inicio TEXT, Data_Fim TEXT, Solicitante TEXT, Email TEXT, Telefone TEXT, Endereco TEXT, Observacoes TEXT, Info_para_DEPOE TEXT)'
            
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(table_sql)
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)


    def id_gen(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute('SELECT COUNT(*) FROM tb_pedidos').fetchone()[0] + 1   
            return rs
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)        


    def insert(self, p):
        try:
            sql_string = f"INSERT INTO tb_pedidos VALUES ({p.code}, '{p.register_date}', '{p.assisted}', '{p.need}', '{p.age}', '{p.beginning}', '{p.ending}', '{p.requester}', '{p.email}', '{p.phone}', '{p.address}', '{p.observations}', '{p.info}')"

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(sql_string)
            conn.commit()

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Pedido de oração cadastrado com sucesso!')
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)     


    def select(self, i):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            rs = cursor.execute(f'SELECT * FROM tb_pedidos WHERE ID = {i}').fetchone()
            return rs     
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn, cursor)
            
            
    def gen_csv(self, p):
        try:
            data = datetime.datetime.now().strftime("%d-%m-%y")

            conn = db.create_connection()
            db_df = pd.read_sql_query(f"SELECT * FROM tb_pedidos WHERE ID >= {p.code}", conn)

            if platform.system() == 'Linux':
                db_df.to_excel(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL/Pedidos_EXCEL_' + data +'.xlsx', index=False, header=True)
            else:
                db_df.to_excel(os.path.expanduser("~") + '\\Desktop\\Pedidos_AELMAC\\EXCEL\\Pedidos_EXCEL_' + data +'.xlsx', index=False, header=True)

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Relatório para EXCEL gerado com sucesso!')        
            tkinter.Tk().destroy()
            
            db.close_connection(conn)
        except sql.Error as e:
            print(e)
        
    
    def gen_pdf(self, p):
        try:
            conn = db.create_connection()
            
            sql_string = f"SELECT * FROM tb_pedidos WHERE ID = {p.code}"
            
            lista_query = conn.execute(sql_string).fetchone()
            
            resultados = []
            for item in lista_query:                
                resultados.append(str(item))
                    
            campos = ['ID', 'Data de Cadastro', 'Assistido', 'Necessidade', 'Idade', 'Data de Início', 'Data de Término', 'Solicitante', 'E-mail', 'Telefone', 'Endereço', 'Observações', 'Info para DEPOE']
            
            pdf = fpdf.FPDF(format='A4')
            pdf.add_page()
            pdf.set_font('times', 'B',size = 20)
            pdf.set_fill_color(200,200,200)
            pdf.write(15,'PEDIDO DE ORAÇÃO - Nº{} Reg. em {}'.format(resultados[0], resultados[1]))      
            pdf.ln()  
            
            i = 2
            while i < len(campos):
                if resultados[i] != 'Não' and resultados[i] != '' and resultados[i] != '()':
                    pdf.set_font('helvetica', 'B',size = 12)                    
                    pdf.cell(55, 12, campos[i].upper(), 1, 0, '', 1, '')
                    pdf.set_font('helvetica', size = 12)
                    pdf.multi_cell(0, 12, resultados[i], 1, 'J', 0)
                    #pdf.ln()
                i += 1
                
                
            if platform.system() == 'Linux':    
                pdf.output(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/PDF/Pedido_' + resultados[0] + '.pdf')
            else:
                pdf.output(os.path.expanduser("~") + '\\Desktop\\Pedidos_AELMAC\\PDF\\Pedido_' + resultados[0] + '.pdf')


            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'PDF do Pedido gerado com sucesso!')
            tkinter.Tk().destroy()
        except sql.Error as e:
            print(e)
        finally:
            db.close_connection(conn)
            
    
    def create_directories(self):
        if not os.path.exists(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC'):
            os.mkdir(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC')
            
        if not os.path.exists(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL'):
            os.mkdir(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/EXCEL')

        if not os.path.exists(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/PDF'):
            os.mkdir(os.path.expanduser("~") + '/Documentos/Pedidos_AELMAC/PDF')
                
            