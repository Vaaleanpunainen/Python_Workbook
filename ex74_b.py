print("\n".join(("{:>4}"*11).format(*(i*j if i*j else i+j if i+j else "" for j in range(11))) for i in range(11)))
