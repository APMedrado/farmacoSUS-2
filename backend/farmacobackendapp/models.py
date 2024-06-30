import mongoengine as me

class Farmaco(me.Document):
    codigo_barra = me.StringField(required=True, primary_key=True)
    produto = me.StringField(required=True, max_length=100)
    principio_ativo = me.StringField(required=True, max_length=100)
    tipo_receita = me.StringField(required=True, max_length=100)
    indicacao = me.StringField(required=True)
    laboratorio = me.StringField(required=True, max_length=100)

    def __str__(self):
        return self.produto

class PostoDistribuicao(me.Document):
    cnes = me.StringField(required=True, primary_key=True)
    nome = me.StringField(required=True, max_length=100)
    municipio = me.StringField(required=True, max_length=100)
    endereco = me.StringField(required=True, max_length=100)
    bairro = me.StringField(required=True, max_length=100)

    def __str__(self):
        return self.nome

class EstoqueLocal(me.Document):
    medicamento = me.ReferenceField(Farmaco, required=True)
    quantidade = me.IntField(required=True)
    quantidade_a_receber = me.IntField(default=0)
    posto_distribuicao = me.ReferenceField(PostoDistribuicao, required=True)

    def __str__(self):
        return f"{self.medicamento} - {self.posto_distribuicao} - {self.quantidade} un"

class EstoqueRegional(me.Document):
    medicamento = me.ReferenceField(Farmaco, required=True)
    quantidade = me.IntField(required=True)

    def __str__(self):
        return f"{self.medicamento} - Regional - {self.quantidade} un"

class Paciente(me.Document):
    cpf = me.StringField(required=True, primary_key=True)
    nome = me.StringField(required=True, max_length=100)
    data_nascimento = me.DateField(required=True)
    bolsa_familia = me.StringField(required=True, max_length=100)
    cadastro_unico = me.StringField(required=True, max_length=100)

    def __str__(self):
        return self.nome

class Medico(me.Document):
    crm = me.StringField(required=True, primary_key=True)
    nome = me.StringField(required=True, max_length=100)
    especialidade = me.StringField(required=True, max_length=100)
    situacao = me.StringField(required=True, max_length=100)

    def __str__(self):
        return self.nome

class RegistroEntrega(me.Document):
    beneficiario = me.ReferenceField(Paciente, required=True)
    receita_medico = me.ReferenceField(Medico, required=True)
    receita_data = me.DateField(required=True)
    posto_distribuicao = me.ReferenceField(PostoDistribuicao, required=True)
    data_entrega = me.DateField(required=True)
    medicamentos = me.ListField(me.DictField(), required=True)

    def __str__(self):
        return f"{self.beneficiario.nome} - {self.data_entrega}"

class LowStockAlert(me.Document):
    medicamento = me.ReferenceField(Farmaco, required=True)
    posto_distribuicao = me.ReferenceField(PostoDistribuicao, required=True)
    quantidade = me.IntField(required=True)
    timestamp = me.DateTimeField(required=True)
    status = me.StringField(required=True, max_length=100)

    def __str__(self):
        return f"{self.medicamento} - {self.posto_distribuicao} - {self.quantidade}"  
    
    
class NotificacaoAbastecimento(me.Document):
    paciente = me.ReferenceField(Paciente, required=True)
    farmaco = me.ReferenceField(Farmaco, requered=True)
    cnes_posto = me.StringField(required=True)
    
    def __str__(self):
        return f"{self.paciente} - {self.farmaco} - {self.cnes}" 

    