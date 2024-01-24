from fpdf import FPDF
def gerar_pdf(Cliente, Servico, Preco, Descricao):    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial')
    pdf.set_text_color(255,255,255)
    pdf.image('img/Orcamento.png', x=0, y=0)

    pdf.text(85,155,Cliente)
    pdf.text(85,175, Servico)
    pdf.text(85,195,f'R$ {Preco}')
    pdf.text(85,215,Descricao)
    
    pdf.output('PDF/orcamento.pdf')
    

    
    