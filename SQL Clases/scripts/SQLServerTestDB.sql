create database TestDB
go
use TestDB
go
create table TestTable(
	[id] int primary key,
	[name] varchar(50),
	[date] datetime
)