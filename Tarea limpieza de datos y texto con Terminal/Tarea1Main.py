cd "/mnt/c/Users/leona/terminaltruco/TC2004B-Leonardo-Orozco/notebook/Tarea limpieza de datos y texto con Terminal/tarea_texto"
mkdir datos salida_texto
rm datos/quijote.txt
curl -L -A "Mozilla/5.0" datos/quijote.txt "https://www.gutenberg.org/cache/epub/2000/pg2000.txt" #(el -L y -A me los sugirio copilot porque sino tronaba)
head -n 5 datos/quijote.txt
grep -n -m 1 "\*\*\* START OF" datos/quijote.txt
grep -n -m 1 "\*\*\* END OF"   datos/quijote.txt
sed -n '/\*\*\* START OF/,/\*\*\* END OF/p' datos/quijote.txt | sed '1d;$d' > salida_texto/quijote_limpio.txt
{
  echo "TOTAL_PALABRAS:"
  awk '{total += NF} END {print total}' salida_texto/quijote_limpio.txt

  echo -e "\nMIN_MAX_PROM_PALABRAS_POR_LINEA:"
  awk 'NR==1 {min=max=NF} {if(NF<min) min=NF; if(NF>max) max=NF; sum+=NF; n++} END {print "min",min,"max",max,"avg",sum/n}' salida_texto/quijote_limpio.txt

  echo -e "\nPROM_LONGITUD_PALABRA:"
  awk '{for(i=1;i<=NF;i++) sum+=length($i); n+=NF} END {print sum/n}' salida_texto/quijote_limpio.txt
} > salida_texto/estadisticas.txt
tr '[:upper:]' '[:lower:]' < salida_texto/quijote_limpio.txt \
  | tr -cs '[:alpha:]' '\n' \
  | sort \
  | uniq -c \
  | sort -rn \
  | head -20 > salida_texto/top20.txt
echo "=== ESTADISTICAS ==="
cat salida_texto/estadisticas.txt
echo -e "\n=== TOP 20 ==="
cat salida_texto/top20.txt


#ESTADISTICAS
TOTAL_PALABRAS:
392365

MIN_MAX_PROM_PALABRAS_POR_LINEA:
min 1 max 20 avg 10.4128

PROM_LONGITUD_PALABRA:
4.4755

OP 20
4.4755

TOP 20
  20769 que
  18410 de
  18410 de
  18280 y
  15642 a
  10528 la
   8295 en
   8271 el
   7035 se
   6387 no
   4776 los
   4275 con
   4195 n
   4116 s
   3945 por
   3707 lo
   3702 le
   3492 las
   3389 su
   3150 m
   2714 don

#Reflexion Critica:
##Considero que hacer este analisis puede llegar a tener sus virtudes, por ejemplo, extraer esta informacion puede ser util.
##Estos datos pueden darnos una idea de la forma de escribir del autor, o incluso de la epoca en la que se escribio el libro.
##Otro ejemplo util seria que con la investigaciona decuada podria ayudar a rastrear signos cerebrales de algun transtorno (por decir algun ejemplo de las capacidades de este analisis).

##Sin embargo, sin un contexto claro no se tiene un significado verdaderamente relevante, por la falta de la parte humana en este analisis,
##los datos no nos pueden decir mucho, porque para empezar nisiquiera conocemos el sentido con el que se empleo.
##Incluso siguiendo su propia logica este analisis limitado no toma en cuenta por ejemplo variantes (caballo, caballos,dejo, decia, etc).
##De esta forma es mas complejo encontrar una relacion entre una cosa y otra