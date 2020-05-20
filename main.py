# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from dto import Pedidos
from dao import Dao
from tkinter import messagebox
import tkinter
import sys
import datetime

p = Pedidos()
dao = Dao()

class Ui_FormPedidos(object):
    ############################################################
    # Form variables
    ############################################################    
    index = 0
    message = ''


    ############################################################
    # Passive methods
    ############################################################    
    def disable_readOnly(self):
        self.txtAssistido.setReadOnly(False)
        self.cmbNecessidade.setEnabled(True)
        self.txtIdade.setReadOnly(False)
        self.txtInicio.setReadOnly(False)
        self.txtFim.setReadOnly(False)
        self.txtSolicitante.setReadOnly(False)
        self.txtEmail.setReadOnly(False)
        self.txtTelefone.setReadOnly(False)
        self.txtEndereco.setReadOnly(False)
        self.txtObs.setReadOnly(False)
        self.checkAcidentes.setEnabled(True)
        self.checkPsiquiatrico.setEnabled(True)
        self.checkDependencia.setEnabled(True)
        self.checkDesemprego.setEnabled(True)
        self.checkHospital.setEnabled(True)
        self.checkCirurgia.setEnabled(True)
        self.checkFalecimento.setEnabled(True)
        self.checkPreso.setEnabled(True)
        self.checkObsessivo.setEnabled(True)
        self.checkDesaparecimento.setEnabled(True)
        self.checkSequestro.setEnabled(True)
        self.checkSuicidio.setEnabled(True)
        self.checkDepressao.setEnabled(True)
        self.checkOutro.setEnabled(True)

    def enable_readOnly(self):
        self.txtAssistido.setReadOnly(True)
        self.cmbNecessidade.setEnabled(False)
        self.txtIdade.setReadOnly(True)
        self.txtInicio.setReadOnly(True)
        self.txtFim.setReadOnly(True)
        self.txtSolicitante.setReadOnly(True)
        self.txtEmail.setReadOnly(True)
        self.txtTelefone.setReadOnly(True)
        self.txtEndereco.setReadOnly(True)
        self.txtObs.setReadOnly(True)
        self.checkAcidentes.setEnabled(False)
        self.checkPsiquiatrico.setEnabled(False)
        self.checkDependencia.setEnabled(False)
        self.checkDesemprego.setEnabled(False)
        self.checkHospital.setEnabled(False)
        self.checkCirurgia.setEnabled(False)
        self.checkFalecimento.setEnabled(False)
        self.checkPreso.setEnabled(False)
        self.checkObsessivo.setEnabled(False)
        self.checkDesaparecimento.setEnabled(False)
        self.checkSequestro.setEnabled(False)
        self.checkSuicidio.setEnabled(False)
        self.checkDepressao.setEnabled(False)
        self.checkOutro.setEnabled(False)
        self.txtOutro.setReadOnly(True)

    def enable_navigation(self):
        self.btnFirst.setEnabled(True)
        self.btnPrevious.setEnabled(True)
        self.btnNext.setEnabled(True)
        self.btnLast.setEnabled(True)

    def disable_navigation(self):
        self.btnFirst.setEnabled(False)
        self.btnPrevious.setEnabled(False)
        self.btnNext.setEnabled(False)
        self.btnLast.setEnabled(False)

    def enable_export(self):
        self.btnExportAll.setEnabled(True)
        self.btnExportOne.setEnabled(True)

    def disable_export(self):
        self.btnExportAll.setEnabled(False)
        self.btnExportOne.setEnabled(False)

    def clear_form(self):
        self.txtAssistido.setText('')

        self.txtIdade.setText('')
        self.txtInicio.setText('')
        self.txtFim.setText('')
        self.txtSolicitante.setText('')
        self.txtEmail.setText('')
        self.txtTelefone.setText('')
        self.txtEndereco.setText('')
        self.txtObs.setText('')

        if self.checkAcidentes.isChecked():
            self.checkAcidentes.toggle()

        if self.checkPsiquiatrico.isChecked():
            self.checkPsiquiatrico.toggle()

        if self.checkDependencia.isChecked():
            self.checkDependencia.toggle()

        if self.checkDesemprego.isChecked():
            self.checkDesemprego.toggle()

        if self.checkHospital.isChecked():
            self.checkHospital.toggle()

        if self.checkCirurgia.isChecked():
            self.checkCirurgia.toggle()

        if self.checkFalecimento.isChecked():
            self.checkFalecimento.toggle()

        if self.checkPreso.isChecked():
            self.checkPreso.toggle()

        if self.checkObsessivo.isChecked():
            self.checkObsessivo.toggle()

        if self.checkDesaparecimento.isChecked():
            self.checkDesaparecimento.toggle()

        if self.checkSequestro.isChecked():
            self.checkSequestro.toggle()

        if self.checkSuicidio.isChecked():
            self.checkSuicidio.toggle()

        if self.checkDepressao.isChecked():
            self.checkDepressao.toggle()

        if self.checkOutro.isChecked():
            self.checkOutro.toggle()

        self.txtOutro.setReadOnly(True)
        self.txtOutro.setText('')

    def fill_form(self):
        self.clear_form()
        results = []
        results = dao.select(self.index)
        
        p.code = results[0]
        p.register_date = results[1]
        p.assisted = results[2]
        p.need = results[3]
        p.age = results[4]
        p.beginning = results[5]
        p.ending = results[6]
        p.requester = results[7]
        p.email = results[8]
        p.phone = results[9]
        p.address = results[10]
        p.observations = results[11]
        p.info = results[12]        
        
        
        self.txtAssistido.setText(p.assisted)

        self.cmbNecessidade.setCurrentText(p.need)

        self.txtIdade.setText(p.age)
        self.txtInicio.setText(p.beginning)
        self.txtFim.setText(p.ending)
        self.txtSolicitante.setText(p.requester)
        self.txtEmail.setText(p.email)
        self.txtTelefone.setText(p.phone)
        self.txtEndereco.setText(p.address)
        self.txtObs.setText(p.observations)

        if p.info.find('Acidentes') != -1:
            self.checkAcidentes.toggle()

        if p.info.find('Caso psiquiátrico') != -1:
            self.checkPsiquiatrico.toggle()

        if p.info.find('Dependências') != -1:
            self.checkDependencia.toggle()

        if p.info.find('Desemprego') != -1:
            self.checkDesemprego.toggle()

        if p.info.find('Hospitalização') != -1:
            self.checkHospital.toggle()

        if p.info.find('Cirurgia') != -1:
            self.checkCirurgia.toggle()

        if p.info.find('Falecimento') != -1:
            self.checkFalecimento.toggle()

        if p.info.find('Preso') != -1:
            self.checkPreso.toggle()

        if p.info.find('Problema obsessivo') != -1:
            self.checkObsessivo.toggle()

        if p.info.find('Desaparecimento') != -1:
            self.checkDesaparecimento.toggle()

        if p.info.find('Sequestro') != -1:
            self.checkSequestro.toggle()

        if p.info.find('Tentativa de suicídio') != -1:
            self.checkSuicidio.toggle()

        if p.info.find('Depressão') != -1:
            self.checkDepressao.toggle()

        if p.info.find(' --- ') != -1:
            self.checkOutro.toggle()
            self.txtOutro.setText(p.info.split(' --- ')[1])
        else:
            self.txtOutro.setText('')
        self.txtOutro.setReadOnly(True)

    def check_fields(self):
        self.message = ''
        
        if len(self.txtAssistido.text().strip()) < 3:
            self.message += '- Nome do assistido inválido\n'
            
        if not self.txtIdade.text().isdigit() and len(self.txtIdade.text().strip()) < 1:
            self.message += '- Idade inválida\n'            
            
        if len(self.txtFim.text()) < len(self.txtInicio.text()) or not self.check_date(self.txtFim.text().strip()) or self.txtFim.text() == self.txtInicio.text():
            self.message += '- Data de Término inválida\n'
            
        if len(self.txtSolicitante.text().strip()) < 3:
            self.message += '- Nome do Solicitante inválido'
            
        if len(self.message) >= 1:
            return True
        else:
            return False
 
    def check_date(self, data):
            import datetime
            
            today = datetime.datetime.now()        
            
            date = data.split('/')
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            
            if year < today.year:
                return False
            else:
                if month > 12 or month < 1:
                    return False
                else:
                    if day < 1:
                        return False
                    else:
                        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                            if day > 31:
                                return False
                        elif month == 2:
                            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                                if day > 29:
                                    return False
                            else:
                                if day > 28:
                                    return False
                        else:
                            if day > 30:
                                return False
            return True
                    
    def treat_fields(self):
        if self.check_fields():
            root = tkinter.Tk()
            root.withdraw()
            
            messagebox.showerror('ERRO', 'ERRO, Não é possível concluir o cadastro devido os seguintes erros:\n\n' + self.message)            
            tkinter.Tk().destroy()
            self.txtAssistido.setFocus()
        else:
            root = tkinter.Tk()
            root.withdraw()
            
            choice = messagebox.askyesno('CONFIRMAR REGISTRO', 'Deseja cadastrar esse pedido?')
            tkinter.Tk().destroy()
            if choice == True:    
                today = datetime.datetime.now().strftime("%d/%m/%Y")

                p.code = dao.id_gen()
                p.register_date = today
                p.assisted = self.txtAssistido.text().strip().title()
                p.need = self.cmbNecessidade.currentText()

                p.age = self.txtIdade.text().strip()
                p.beginning = self.txtInicio.text().strip()
                p.ending = self.txtFim.text().strip()
                p.requester = self.txtSolicitante.text().strip().title()
                p.email = self.txtEmail.text().strip()
                p.phone = self.txtTelefone.text().strip()
                p.address = self.txtEndereco.text().strip().title()
                p.observations = self.txtObs.toPlainText().strip()
                                
                infos = ''                
                
                if self.checkAcidentes.isChecked():
                    infos += 'Acidentes, '
                if self.checkPsiquiatrico.isChecked():
                    infos += 'Caso psiquiátrico, '
                if self.checkDependencia.isChecked():
                    infos += 'Dependências, '
                if self.checkDesemprego.isChecked():
                    infos += 'Desemprego, '
                if self.checkHospital.isChecked():
                    infos += 'Hospitalização, '
                if self.checkCirurgia.isChecked():
                    infos += 'Cirurgia, '
                if self.checkFalecimento.isChecked():
                    infos += 'Falecimento, '
                if self.checkPreso.isChecked():
                    infos += 'Preso, '
                if self.checkObsessivo.isChecked():
                    infos += 'Problema obsessivo, '
                if self.checkDesaparecimento.isChecked():
                    infos += 'Desaparecimento, '
                if self.checkSequestro.isChecked():
                    infos += 'Sequestro, '
                if self.checkSuicidio.isChecked():
                    infos += 'Tentativa de suicídio, '
                if self.checkDepressao.isChecked():
                    infos += 'Depressão'
                
                if infos.endswith(', '):
                    infos = infos[:-2]
                
                if len(self.txtOutro.toPlainText()) > 2:
                    infos += ' --- ' + self.txtOutro.toPlainText()
                
                p.info = infos
                
                dao.insert(p)
                self.btn_add_clicked()
                self.enable_export()

    def navigation_buttons(self):
        total = dao.id_gen() - 1

        if total <= 1:
            self.disable_navigation()
            self.disable_export()
        else:
            if self.index == 1 and total != 1:
                self.btnFirst.setEnabled(False)
                self.btnPrevious.setEnabled(False)
                self.btnNext.setEnabled(True)
                self.btnLast.setEnabled(True)
            elif self.index == total and total > 1:
                self.btnFirst.setEnabled(True)
                self.btnPrevious.setEnabled(True)
                self.btnNext.setEnabled(False)
                self.btnLast.setEnabled(False)
            else:
                self.btnFirst.setEnabled(True)
                self.btnPrevious.setEnabled(True)
                self.btnNext.setEnabled(True)
                self.btnLast.setEnabled(True)

        self.lblIndex.setText(str(self.index))
        self.lblTotal.setText(str(total))



    ############################################################
    # buttons methods
    ############################################################    
    def btn_add_clicked(self):
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        
        if self.txtAssistido.isReadOnly():
            self.disable_readOnly()
            self.disable_navigation()
            self.disable_export()
            self.clear_form()

            self.btnSave.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnAdd.setIcon(icon)
            self.btnAdd.setIconSize(QtCore.QSize(24, 24))
            self.btnAdd.setText("CANCELAR")
            self.btnSave.setEnabled(True)
            self.txtAssistido.setFocus(True)
            self.txtInicio.setText(today)
            self.txtInicio.setReadOnly(True)
        else:
            self.enable_readOnly()
            self.enable_navigation()
            self.enable_export()
            self.fill_form()
            self.btn_last_clicked()

            self.btnSave.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnAdd.setIcon(icon)
            self.btnAdd.setIconSize(QtCore.QSize(24, 24))
            self.btnAdd.setText("ADICIONAR")
            self.btnSave.setEnabled(False)

    def check_outro_clicked(self):
        if self.checkOutro.isChecked():
            self.txtOutro.setEnabled(True)
            self.txtOutro.setReadOnly(False)
        else:
            self.txtOutro.setReadOnly(True)
            self.txtOutro.setText('')

    def btn_save_clicked(self):
        self.treat_fields()

    def btn_first_clicked(self):
        self.index = 1
        dao.select(self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_previous_clicked(self):
        self.index -= 1
        dao.select(self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_next_clicked(self):
        self.index += 1
        dao.select(self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_last_clicked(self):
        self.index = dao.id_gen() - 1
        dao.select(self.index)
        self.fill_form()
        self.navigation_buttons()

    def btn_export_all_clicked(self):
        root = tkinter.Tk()
        root.withdraw()
        
        choice = messagebox.askyesno('EXPORTAR PARA EXCEL', 'Deseja criar relatório com os pedidos a partir do pedido Nº' + str(p.code) + '?')
        tkinter.Tk().destroy()
        if choice == True:    
            dao.gen_csv(p)
    
    def btn_export_one_clicked(self):
        dao.gen_pdf(p)
     
     
        
    ############################################################
    # QT Designer methods
    ############################################################    
    def setupUi(self, FormPedidos):
        FormPedidos.setObjectName("FormPedidos")
        FormPedidos.resize(800, 665)
        FormPedidos.setMaximumSize(QtCore.QSize(800, 665))
        FormPedidos.setMinimumSize(QtCore.QSize(800, 665))
        self.centralwidget = QtWidgets.QWidget(FormPedidos)
        self.centralwidget.setObjectName("centralwidget")
        self.lblAssistido = QtWidgets.QLabel(self.centralwidget)
        self.lblAssistido.setGeometry(QtCore.QRect(10, 10, 551, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAssistido.setFont(font)
        self.lblAssistido.setObjectName("lblAssistido")
        self.txtAssistido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAssistido.setGeometry(QtCore.QRect(10, 30, 550, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtAssistido.setFont(font)
        self.txtAssistido.setObjectName("txtAssistido")
        self.lblIdade = QtWidgets.QLabel(self.centralwidget)
        self.lblIdade.setGeometry(QtCore.QRect(10, 125, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblIdade.setFont(font)
        self.lblIdade.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIdade.setObjectName("lblIdade")
        self.txtIdade = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIdade.setGeometry(QtCore.QRect(10, 150, 150, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtIdade.setFont(font)
        self.txtIdade.setAlignment(QtCore.Qt.AlignCenter)
        self.txtIdade.setObjectName("txtIdade")
        self.gpInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.gpInfo.setGeometry(QtCore.QRect(570, 10, 221, 525))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.gpInfo.setFont(font)
        self.gpInfo.setObjectName("gpInfo")
        self.checkAcidentes = QtWidgets.QCheckBox(self.gpInfo)
        self.checkAcidentes.setGeometry(QtCore.QRect(10, 30, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkAcidentes.setFont(font)
        self.checkAcidentes.setObjectName("checkAcidentes")
        self.checkPsiquiatrico = QtWidgets.QCheckBox(self.gpInfo)
        self.checkPsiquiatrico.setGeometry(QtCore.QRect(10, 55, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkPsiquiatrico.setFont(font)
        self.checkPsiquiatrico.setObjectName("checkPsiquiatrico")
        self.checkDependencia = QtWidgets.QCheckBox(self.gpInfo)
        self.checkDependencia.setGeometry(QtCore.QRect(10, 80, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDependencia.setFont(font)
        self.checkDependencia.setObjectName("checkDependencia")
        self.checkDesemprego = QtWidgets.QCheckBox(self.gpInfo)
        self.checkDesemprego.setGeometry(QtCore.QRect(10, 105, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDesemprego.setFont(font)
        self.checkDesemprego.setObjectName("checkDesemprego")
        self.checkHospital = QtWidgets.QCheckBox(self.gpInfo)
        self.checkHospital.setGeometry(QtCore.QRect(10, 130, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkHospital.setFont(font)
        self.checkHospital.setObjectName("checkHospital")
        self.checkCirurgia = QtWidgets.QCheckBox(self.gpInfo)
        self.checkCirurgia.setGeometry(QtCore.QRect(10, 155, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkCirurgia.setFont(font)
        self.checkCirurgia.setObjectName("checkCirurgia")
        self.checkFalecimento = QtWidgets.QCheckBox(self.gpInfo)
        self.checkFalecimento.setGeometry(QtCore.QRect(10, 180, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkFalecimento.setFont(font)
        self.checkFalecimento.setObjectName("checkFalecimento")
        self.checkPreso = QtWidgets.QCheckBox(self.gpInfo)
        self.checkPreso.setGeometry(QtCore.QRect(10, 205, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkPreso.setFont(font)
        self.checkPreso.setObjectName("checkPreso")
        self.checkObsessivo = QtWidgets.QCheckBox(self.gpInfo)
        self.checkObsessivo.setGeometry(QtCore.QRect(10, 230, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkObsessivo.setFont(font)
        self.checkObsessivo.setObjectName("checkObsessivo")
        self.checkDesaparecimento = QtWidgets.QCheckBox(self.gpInfo)
        self.checkDesaparecimento.setGeometry(QtCore.QRect(10, 255, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDesaparecimento.setFont(font)
        self.checkDesaparecimento.setObjectName("checkDesaparecimento")
        self.checkSequestro = QtWidgets.QCheckBox(self.gpInfo)
        self.checkSequestro.setGeometry(QtCore.QRect(10, 280, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkSequestro.setFont(font)
        self.checkSequestro.setObjectName("checkSequestro")
        self.checkSuicidio = QtWidgets.QCheckBox(self.gpInfo)
        self.checkSuicidio.setGeometry(QtCore.QRect(10, 305, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkSuicidio.setFont(font)
        self.checkSuicidio.setObjectName("checkSuicidio")
        self.checkDepressao = QtWidgets.QCheckBox(self.gpInfo)
        self.checkDepressao.setGeometry(QtCore.QRect(10, 330, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkDepressao.setFont(font)
        self.checkDepressao.setObjectName("checkDepressao")
        self.checkOutro = QtWidgets.QCheckBox(self.gpInfo)
        self.checkOutro.setGeometry(QtCore.QRect(10, 355, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkOutro.setFont(font)
        self.checkOutro.setObjectName("checkOutro")
        self.txtOutro = QtWidgets.QTextEdit(self.gpInfo)
        self.txtOutro.setGeometry(QtCore.QRect(10, 380, 201, 135))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtOutro.setFont(font)
        self.txtOutro.setObjectName("txtOutro")
        self.txtInicio = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInicio.setGeometry(QtCore.QRect(210, 150, 151, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtInicio.setFont(font)
        self.txtInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.txtInicio.setObjectName("txtInicio")
        self.lblInicio = QtWidgets.QLabel(self.centralwidget)
        self.lblInicio.setGeometry(QtCore.QRect(215, 124, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblInicio.setFont(font)
        self.lblInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInicio.setObjectName("lblInicio")
        self.lblFim = QtWidgets.QLabel(self.centralwidget)
        self.lblFim.setGeometry(QtCore.QRect(416, 124, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblFim.setFont(font)
        self.lblFim.setObjectName("lblFim")
        self.txtFim = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFim.setGeometry(QtCore.QRect(410, 150, 151, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtFim.setFont(font)
        self.txtFim.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFim.setObjectName("txtFim")
        self.lblSolicitante = QtWidgets.QLabel(self.centralwidget)
        self.lblSolicitante.setGeometry(QtCore.QRect(10, 200, 551, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblSolicitante.setFont(font)
        self.lblSolicitante.setObjectName("lblSolicitante")
        self.txtSolicitante = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSolicitante.setGeometry(QtCore.QRect(10, 220, 550, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtSolicitante.setFont(font)
        self.txtSolicitante.setObjectName("txtSolicitante")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(10, 290, 361, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(10, 270, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.lblTelefone = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefone.setGeometry(QtCore.QRect(390, 270, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblTelefone.setFont(font)
        self.lblTelefone.setObjectName("lblTelefone")
        self.txtTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefone.setGeometry(QtCore.QRect(390, 290, 171, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtTelefone.setFont(font)
        self.txtTelefone.setObjectName("txtTelefone")
        self.lblEndereco = QtWidgets.QLabel(self.centralwidget)
        self.lblEndereco.setGeometry(QtCore.QRect(10, 340, 551, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblEndereco.setFont(font)
        self.lblEndereco.setObjectName("lblEndereco")
        self.txtEndereco = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEndereco.setGeometry(QtCore.QRect(10, 360, 551, 32))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.txtEndereco.setFont(font)
        self.txtEndereco.setObjectName("txtEndereco")
        self.lblObs = QtWidgets.QLabel(self.centralwidget)
        self.lblObs.setGeometry(QtCore.QRect(10, 410, 551, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblObs.setFont(font)
        self.lblObs.setObjectName("lblObs")
        self.txtObs = QtWidgets.QTextEdit(self.centralwidget)
        self.txtObs.setGeometry(QtCore.QRect(10, 430, 551, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtObs.setFont(font)
        self.txtObs.setObjectName("txtObs")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(700, 545, 91, 34))
        self.btnSave.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QtCore.QSize(24, 24))
        self.btnSave.setObjectName("btnSave")
        self.btnExportAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportAll.setGeometry(QtCore.QRect(570, 625, 221, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExportAll.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/page_excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportAll.setIcon(icon1)
        self.btnExportAll.setIconSize(QtCore.QSize(24, 24))
        self.btnExportAll.setObjectName("btnExportAll")
        self.btnExportOne = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportOne.setGeometry(QtCore.QRect(570, 585, 221, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExportOne.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/page_white_acrobat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExportOne.setIcon(icon2)
        self.btnExportOne.setIconSize(QtCore.QSize(24, 24))
        self.btnExportOne.setObjectName("btnExportOne")
        self.gpNavegacao = QtWidgets.QGroupBox(self.centralwidget)
        self.gpNavegacao.setGeometry(QtCore.QRect(10, 549, 551, 111))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.gpNavegacao.setFont(font)
        self.gpNavegacao.setObjectName("gpNavegacao")
        self.btnFirst = QtWidgets.QPushButton(self.gpNavegacao)
        self.btnFirst.setGeometry(QtCore.QRect(10, 70, 95, 34))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/resultset_first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFirst.setIcon(icon3)
        self.btnFirst.setObjectName("btnFirst")
        self.btnPrevious = QtWidgets.QPushButton(self.gpNavegacao)
        self.btnPrevious.setGeometry(QtCore.QRect(160, 70, 100, 34))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/resultset_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrevious.setIcon(icon4)
        self.btnPrevious.setObjectName("btnPrevious")
        self.lblIndex = QtWidgets.QLabel(self.gpNavegacao)
        self.lblIndex.setGeometry(QtCore.QRect(170, 32, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblIndex.setFont(font)
        self.lblIndex.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIndex.setObjectName("lblIndex")
        self.lblTotal = QtWidgets.QLabel(self.gpNavegacao)
        self.lblTotal.setGeometry(QtCore.QRect(304, 32, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblTotal.setFont(font)
        self.lblTotal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotal.setObjectName("lblTotal")
        self.label_12 = QtWidgets.QLabel(self.gpNavegacao)
        self.label_12.setGeometry(QtCore.QRect(256, 32, 43, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btnNext = QtWidgets.QPushButton(self.gpNavegacao)
        self.btnNext.setGeometry(QtCore.QRect(300, 70, 95, 34))
        self.btnNext.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/resultset_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon5)
        self.btnNext.setObjectName("btnNext")
        self.btnLast = QtWidgets.QPushButton(self.gpNavegacao)
        self.btnLast.setGeometry(QtCore.QRect(445, 70, 95, 34))
        self.btnLast.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/resultset_last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLast.setIcon(icon6)
        self.btnLast.setObjectName("btnLast")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(570, 545, 121, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon7)
        self.btnAdd.setIconSize(QtCore.QSize(24, 24))
        self.btnAdd.setObjectName("btnAdd")
        self.lblNecessidade = QtWidgets.QLabel(self.centralwidget)
        self.lblNecessidade.setGeometry(QtCore.QRect(10, 85, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblNecessidade.setFont(font)
        self.lblNecessidade.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNecessidade.setObjectName("lblNecessidade")
        self.cmbNecessidade = QtWidgets.QComboBox(self.centralwidget)
        self.cmbNecessidade.setGeometry(QtCore.QRect(130, 80, 431, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmbNecessidade.setFont(font)
        self.cmbNecessidade.setObjectName("cmbNecessidade")
        self.cmbNecessidade.addItem("")
        self.cmbNecessidade.addItem("")
        self.cmbNecessidade.addItem("")
        FormPedidos.setCentralWidget(self.centralwidget)

        
        self.btnAdd.clicked.connect(self.btn_add_clicked)
        self.btnExportAll.clicked.connect(self.btn_export_all_clicked)
        self.btnExportOne.clicked.connect(self.btn_export_one_clicked)
        self.btnFirst.clicked.connect(self.btn_first_clicked)
        self.btnLast.clicked.connect(self.btn_last_clicked)
        self.btnNext.clicked.connect(self.btn_next_clicked)
        self.btnPrevious.clicked.connect(self.btn_previous_clicked)
        self.btnSave.clicked.connect(self.btn_save_clicked)
        self.checkOutro.clicked.connect(self.check_outro_clicked)                
        
        self.enable_readOnly()

        if dao.id_gen() - 1 < 1:
            self.clear_form()                        
            self.navigation_buttons()
        else:
            self.btn_last_clicked()
            self.navigation_buttons()
            self.enable_export()            
        
        self.retranslateUi(FormPedidos)
        QtCore.QMetaObject.connectSlotsByName(FormPedidos)       

    def retranslateUi(self, FormPedidos):
        _translate = QtCore.QCoreApplication.translate
        FormPedidos.setWindowTitle(_translate("FormPedidos", "PEDIDOS DE ORACAO"))
        self.lblAssistido.setText(_translate("FormPedidos", "NOME DO ASSISTIDO"))
        self.lblIdade.setText(_translate("FormPedidos", "IDADE"))
        self.txtIdade.setInputMask(_translate("FormPedidos", "###"))
        self.gpInfo.setTitle(_translate("FormPedidos", "INFO PARA O DEPOE"))
        self.checkAcidentes.setText(_translate("FormPedidos", "Acidentes"))
        self.checkPsiquiatrico.setText(_translate("FormPedidos", "Caso psiquiátrico"))
        self.checkDependencia.setText(_translate("FormPedidos", "Dependências"))
        self.checkDesemprego.setText(_translate("FormPedidos", "Desemprego"))
        self.checkHospital.setText(_translate("FormPedidos", "Hospitalização"))
        self.checkCirurgia.setText(_translate("FormPedidos", "Cirurgia"))
        self.checkFalecimento.setText(_translate("FormPedidos", "Falecimento"))
        self.checkPreso.setText(_translate("FormPedidos", "Preso"))
        self.checkObsessivo.setText(_translate("FormPedidos", "Prob. Obsessivo"))
        self.checkDesaparecimento.setText(_translate("FormPedidos", "Desaparecimento"))
        self.checkSequestro.setText(_translate("FormPedidos", "Sequestro"))
        self.checkSuicidio.setText(_translate("FormPedidos", "Tentativa de Suicídio"))
        self.checkDepressao.setText(_translate("FormPedidos", "Depressão"))
        self.checkOutro.setText(_translate("FormPedidos", "Outro:"))
        self.txtInicio.setInputMask(_translate("FormPedidos", "##/##/####"))
        self.lblInicio.setText(_translate("FormPedidos", "DATA DE INÍCIO"))
        self.lblFim.setText(_translate("FormPedidos", "DATA DE TÉRMINO"))
        self.txtFim.setInputMask(_translate("FormPedidos", "##/##/####"))
        self.lblSolicitante.setText(_translate("FormPedidos", "NOME DO SOLICITANTE"))
        self.lblEmail.setText(_translate("FormPedidos", "E-MAIL"))
        self.lblTelefone.setText(_translate("FormPedidos", "TELEFONE"))
        self.txtTelefone.setInputMask(_translate("FormPedidos", "(##) #########"))
        # self.txtTelefone.setText(_translate("FormPedidos", "() "))
        self.lblEndereco.setText(_translate("FormPedidos", "ENDEREÇO"))
        self.lblObs.setText(_translate("FormPedidos", "OBSERVAÇÕES"))
        self.btnSave.setText(_translate("FormPedidos", "SALVAR"))
        self.btnExportAll.setText(_translate("FormPedidos", "EXPORTAR REGISTROS"))
        self.btnExportOne.setText(_translate("FormPedidos", "EXPORTAR REGISTRO ATUAL"))
        self.gpNavegacao.setTitle(_translate("FormPedidos", "NAVEGAÇÃO"))
        self.btnFirst.setText(_translate("FormPedidos", "PRIMEIRO"))
        self.btnPrevious.setText(_translate("FormPedidos", "ANTERIOR"))
        # self.lblIndex.setText(_translate("FormPedidos", "0"))
        # self.lblTotal.setText(_translate("FormPedidos", "0"))
        self.label_12.setText(_translate("FormPedidos", "DE"))
        self.btnNext.setText(_translate("FormPedidos", "PRÓXIMO"))
        self.btnLast.setText(_translate("FormPedidos", "ÚLTIMO"))
        self.btnAdd.setText(_translate("FormPedidos", "ADICIONAR"))
        self.lblNecessidade.setText(_translate("FormPedidos", "NECESSIDADE"))
        self.cmbNecessidade.setItemText(0, _translate("FormPedidos", "Físico"))
        self.cmbNecessidade.setItemText(1, _translate("FormPedidos", "Desencarnada"))
        self.cmbNecessidade.setItemText(2, _translate("FormPedidos", "Espiritual"))


if __name__ == "__main__":
    import sys
    dao.create_table()    
    dao.create_directories()
    app = QtWidgets.QApplication(sys.argv)
    FormPedidos = QtWidgets.QMainWindow()
    ui = Ui_FormPedidos()
    ui.setupUi(FormPedidos)
    FormPedidos.show()
    sys.exit(app.exec_())
