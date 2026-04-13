create table usuario(nome varchar(100));
create table cidade (cidade varchar(100));

insert into usuario(nome) values('fabricio');
insert into usuario(nome) values('jane');
insert into usuario(nome) values('thales');
insert into usuario(nome) values('eduardo');
insert into usuario(nome) values('fabiola');

insert into cidade(cidade) values('são josé');
insert into cidade(cidade) values('taubaté');
insert into cidade(cidade) values('itatiaia');
insert into cidade(cidade) values('taubaté');
insert into cidade(cidade) values('belém');

select * from usuario, cidade;

select * from usuario;

select * from cidade;


