def main():
    v = (input("Сколько футов:"))
    g = feet2meter(v.replace("ft",""))
    print(f"Это будет " + str(round(g, 2)) +  " метров.")

def feet2meter(g):
    return float(g) * float(0.3048)
	# Здесь будет ваш код

main()
