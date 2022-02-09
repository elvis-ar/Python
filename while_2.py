""" La población actual de una colonia de insectos “A” es de 55 millones y crecea una tasa del 7 % anual. 
La población de otra colonia “B” es de 250millones y crece a razón de  un  2%  anual.  
Si  estas  dos  colonias  mantuvieransu  ritmo  de  crecimiento  actual;  
¿en cuántos años la población “A” será lamitad de la población “B”? """

def main():
    suburb_a = 55000000
    suburb_b = 250000000
    count_years = 0
    flag = 0

    while flag == 0:
        suburb_a += (suburb_a * 0.07)
        suburb_b += (suburb_b * 0.02)
        count_years += 1
        
        if suburb_a >= (suburb_b/2):
            print(f"poblacion A {suburb_a: .2f}")
            print(f"poblacion b {suburb_b: .2f}")
            print(f"la mitad de la poblacion b es {suburb_b / 2: .2f}")
            print(f"la poblacion A alconzo la mitad de la poblacion B a los {count_years} anios ")
            flag = 1

if __name__ == "__main__":
    main()