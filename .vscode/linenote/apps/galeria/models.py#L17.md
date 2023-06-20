# Para filtrar utiliza-se o seguinte campo

items = YourModel.objects.filter(status="CONFECÇÃO", sub_status="CONCLUÍDO")

# Para atualizar o segunte

item.status = "APROVAÇÃO"  # Update the main status to "Aprovação"
item.sub_status = "APROVADA"  # Update the sub-status to "Aprovada"
item.save()  # Save the changes to the database
