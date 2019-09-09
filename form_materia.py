import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from persistencia import *

builder = Gtk.Builder()

def vai_para_registro(n):
    materia1 = Materia.get_by_id(n)
    #materia1 = daom.retornar_materia(n)
    lbl_registro = builder.get_object('lbl_registro')
    lbl_registro.set_text(str(n))
    txt_nome = builder.get_object('txt_nome')
    txt_nota = builder.get_object('txt_nota')
    txt_nome.set_text(materia1.nome)
    txt_nota.set_text(str(materia1.nota))

class Eventos_form_incluir_materia:
    def fechar_modal(self, widget):
        widget.hide()
        return false
        Gtk.main_quit()

    def atualizar_form_materia(self):
        vai_para_registro(1)
        print("ok tela atualizada!!")
        self.window3 = builder.get_object("window1")
        self.window3.show_all()
     
    def btn_acao_incluir_materia(self):
        txt_nome = builder.get_object("txt_novo_nome");
        txt_nota = builder.get_object("txt_novo_nota");
        Materia.create(nome=txt_nome.get_text(), nota= txt_nota.get_text())
        #daom.incluir_materia(Materia(txt_nome.get_text(), txt_nota.get_text()))

        lbl_mensagem = builder.get_object("lbl_mensagem");
        lbl_mensagem.set_text("Materia "+txt_nome.get_text()+ " incluída!")

        txt_nome.set_text("")
        txt_nota.set_text("")

class Eventos_form_materia:

    def fechar(self, *args):
        Gtk.main_quit()

    def btn_primeiro(self, button):
        vai_para_registro(1)

    def btn_proximo(self, button):
        lbl_registro = builder.get_object('lbl_registro')
        #print(lbl_registro)
        vai_para_registro(int(lbl_registro.get_text())+1)

    def btn_incluir(self, button):
        builder.add_from_file("/home/aluno/Xemano/form_nova_materia.glade")
        builder.connect_signals(Eventos_form_incluir_materia)
        self.window2 = builder.get_object("novamateria")
        self.window2.show_all()
        self.window3 = builder.get_object("window1")
        self.window3.hide()

builder.add_from_file("/home/aluno/Xemano/form_materia.glade")
builder.connect_signals(Eventos_form_materia())
window = builder.get_object("window1")
window.show_all()

Gtk.main()