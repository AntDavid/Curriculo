from fpdf import FPDF

class PDF(FPDF):
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body.encode('latin-1', 'replace').decode('latin-1'))
        self.ln()

    def add_section(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

pdf = PDF()

# Personal information
pdf.add_page()
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Antonio David de Jesus Santana', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'São Paulo, São Paulo, Brasil', 0, 1, 'C')
pdf.cell(0, 10, 'davidantoniodavi@gmail.com | +55 11 97388-5768', 0, 1, 'C')
pdf.cell(0, 10, 'LinkedIn: linkedin.com/in/antonlo-davld | GitHub: https://github.com/AntDavid/', 0, 1, 'C')
pdf.ln(10)

# Summary
pdf.chapter_title('Resumo')
summary = ("Desenvolvedor Python, Django, JavaScript, e SQL. Conhecimento em análise de dados com Power BI, Tableau e Excel Avançado. Experiência em integração de sistemas utilizando APIs REST e SOAP, além de manutenção de computadores e redes.")
pdf.chapter_body(summary)

# Experience
pdf.chapter_title('Experiências')
experience = ("Desenvolvedor de Integração\n"
              "Confluence Informática\n"
              "Out 2023 - Nov 2023 (3 meses) - Home Office\n"
              "- Utilização de Caché Object Script e Ensemble para integração de sistemas de saúde.\n\n"
              "Estagiário de TI\n"
              "Escola Vereador Luiz Santos\n"
              "Ago 2019 - Nov 2019 (4 meses)\n"
              "- Manutenção e suporte de informática.\n\n"
              "Atendente de Call Center\n"
              "Tel Centro de Contatos\n"
              "Nov 2021 - Fev 2023\n"
              "- Atendimento ativo e receptivo, agendamento de exames e consultas.")
pdf.chapter_body(experience)

# Education
pdf.chapter_title('Formação Acadêmica')
education = ("Bachelor's em Ciência da Computação\n"
             "UFBRA\n"
             "Jan 2024 - Dez 2027\n\n"
             "Licenciatura em Física\n"
             "IFBA - Instituto Federal da Bahia\n"
             "Ago 2021 - Trancado no 5º Semestre\n\n"
             "Técnico em Informática\n"
             "Instituto Federal de Educação, Ciência e Tecnologia Baiano - IFBAIANO\n"
             "Mai 2017 - Dez 2019")
pdf.chapter_body(education)

# Projects
pdf.chapter_title('Projetos')
projects = ("Feel The Future\n"
            "Plataforma de estudo com flashcards desenvolvida em Django e integrada com SQLite.\n"
            "GitHub Link: https://github.com/AntDavid/prj_feel_the_future_djg\n\n"
            "Uso de Arduino na Determinação da Condutividade Térmica de Metais\n"
            "Experimento de baixo custo utilizando Arduino para medir propriedades térmicas de metais.\n"
            "GitHub Link: https://github.com/AntDavid/prj_feel_the_future_djg")
pdf.chapter_body(projects)

# Certifications
pdf.chapter_title('Certificações')
certifications = ("Google Data Analytics - Google\n"
                  "Análise de Dados com Programação em R - Google\n"
                  "IBM Data Analyst - IBM\n"
                  "Python for Data Science, AI & Development - IBM")
pdf.chapter_body(certifications)

# Technical Skills
pdf.chapter_title('Habilidades Técnicas')
technical_skills = ("Data Analytics\n"
                    "Data Visualization\n"
                    "Python for Data Science\n"
                    "Python Development\n"
                    "C++\n"
                    "C#\n"
                    "Django Framework\n"
                    "Flask.py\n"
                    "NET Framework\n"
                    "Iris Intersystems\n"
                    "Caché Object Script")
pdf.chapter_body(technical_skills)

# Soft Skills
pdf.chapter_title('Soft Skills')
soft_skills = ("Proatividade\n"
               "Pontualidade\n"
               "Trabalho em equipe\n"
               "Idoneidade moral\n"
               "Liderança\n"
               "Facilidade de aprendizado\n"
               "Vontade de aprender novas técnicas")
pdf.chapter_body(soft_skills)

# Output PDF
output_path = "Antonio_David_Santana_Resumo.pdf"
pdf.output(output_path)
