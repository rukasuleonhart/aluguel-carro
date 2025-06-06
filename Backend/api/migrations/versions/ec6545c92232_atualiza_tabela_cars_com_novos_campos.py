"""Atualiza tabela cars com novos campos

Revision ID: ec6545c92232
Revises: 7f98702c7a83
Create Date: 2025-06-06 13:36:31.862242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec6545c92232'
down_revision: Union[str, None] = '7f98702c7a83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Adiciona as colunas como nullable=True para evitar erro com dados existentes
    op.add_column('cars', sa.Column('brand', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('model', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('cars', sa.Column('images', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('cars', sa.Column('speed', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('acceleration', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('fuel', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('transmission', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('horsepower', sa.String(), nullable=True))
    op.add_column('cars', sa.Column('seats', sa.Integer(), nullable=True))

    # Atualiza as colunas para valores padrão para linhas existentes
    op.execute("UPDATE cars SET brand = 'Unknown' WHERE brand IS NULL")
    op.execute("UPDATE cars SET model = 'Unknown' WHERE model IS NULL")
    op.execute("UPDATE cars SET price = 0 WHERE price IS NULL")
    op.execute("UPDATE cars SET images = ARRAY[]::varchar[] WHERE images IS NULL")
    op.execute("UPDATE cars SET speed = '0 km/h' WHERE speed IS NULL")
    op.execute("UPDATE cars SET acceleration = '0 s' WHERE acceleration IS NULL")
    op.execute("UPDATE cars SET fuel = 'Unknown' WHERE fuel IS NULL")
    op.execute("UPDATE cars SET transmission = 'Unknown' WHERE transmission IS NULL")
    op.execute("UPDATE cars SET horsepower = '0' WHERE horsepower IS NULL")
    op.execute("UPDATE cars SET seats = 0 WHERE seats IS NULL")

    # Altera as colunas para NOT NULL após popular os dados
    op.alter_column('cars', 'brand', nullable=False)
    op.alter_column('cars', 'model', nullable=False)
    op.alter_column('cars', 'price', nullable=False)
    op.alter_column('cars', 'images', nullable=False)
    op.alter_column('cars', 'speed', nullable=False)
    op.alter_column('cars', 'acceleration', nullable=False)
    op.alter_column('cars', 'fuel', nullable=False)
    op.alter_column('cars', 'transmission', nullable=False)
    op.alter_column('cars', 'horsepower', nullable=False)
    op.alter_column('cars', 'seats', nullable=False)

    op.drop_index('ix_cars_placa', table_name='cars')
    op.create_index(op.f('ix_cars_id'), 'cars', ['id'], unique=False)
    op.drop_column('cars', 'image_url')
    op.drop_column('cars', 'dia_inicio')
    op.drop_column('cars', 'preco_diaria')
    op.drop_column('cars', 'distancia')
    op.drop_column('cars', 'bairro')
    op.drop_column('cars', 'cidade')
    op.drop_column('cars', 'mes')
    op.drop_column('cars', 'dia_fim')
    op.drop_column('cars', 'nome')
    op.drop_column('cars', 'estado')
    op.drop_column('cars', 'placa')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column('cars', sa.Column('placa', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('estado', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('dia_fim', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('mes', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('cidade', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('bairro', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('distancia', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('preco_diaria', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('dia_inicio', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('cars', sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_cars_id'), table_name='cars')
    op.create_index('ix_cars_placa', 'cars', ['placa'], unique=True)
    op.drop_column('cars', 'seats')
    op.drop_column('cars', 'horsepower')
    op.drop_column('cars', 'transmission')
    op.drop_column('cars', 'fuel')
    op.drop_column('cars', 'acceleration')
    op.drop_column('cars', 'speed')
    op.drop_column('cars', 'images')
    op.drop_column('cars', 'price')
    op.drop_column('cars', 'model')
    op.drop_column('cars', 'brand')
