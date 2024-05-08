# Leer el archivo de texto
lineas <- readLines("prueba/20240108 Mercadona 83,73 €.txt", encoding = "latin1")

# Convertir caracteres a UTF-8
lineas <- lapply(lineas, function(x) iconv(x, from = "latin1", to = "UTF-8"))

# Encontrar la línea que contiene "Descripción P. Unit Importe"
inicio_datos_idx <- which(grepl("Descripción P. Unit Importe", lineas))
if (length(inicio_datos_idx) > 0) {
  inicio_datos <- inicio_datos_idx[1] + 1
} else {
  stop("No se encontró la línea 'Descripción P. Unit Importe' en el archivo de texto.")
}

# Encontrar la línea que contiene "TOTAL"
fin_datos_idx <- which(grepl("TOTAL", lineas))
if (length(fin_datos_idx) > 0) {
  fin_datos <- fin_datos_idx[1] - 1
} else {
  stop("No se encontró la línea 'TOTAL' en el archivo de texto.")
}

# Extraer las líneas de datos
datos <- lineas[inicio_datos:fin_datos]
### 
datos_separados <- lapply(datos, function(x) {
  # Extraer Cantidad (primer número)
  cantidad <- as.numeric(sub("\\D*(\\d+).*", "\\1", x))
  
  # Extraer Descripcion (resto de la cadena)
  descripcion <- gsub("^\\d+([,.]?\\d*)?\\s*", "", x)  # Eliminar números al principio de la cadena
  descripcion <- gsub("\\s+$", "", descripcion)         # Eliminar espacios en blanco al final de la cadena
  
  
  
  
  # Extraer P.Unit (número antes del importe en la descripción)
  p_unit_match <- gregexpr("\\b\\d[\\d,.]*\\b(?!.*\\b\\d[\\d,.]*\\b)", descripcion, perl = TRUE)
  p_unit <- ""
  if (attr(p_unit_match[[1]], "match.length")[1] > 0) {
    p_unit <- substr(descripcion, p_unit_match[[1]][1], p_unit_match[[1]][1] + attr(p_unit_match[[1]], "match.length")[1] - 1)
  }
  
  # Extraer Importe (último número)
  importe <- as.numeric(sub(".*\\b(\\d[\\d,.]*)\\b", "\\1", x))
  
  # Crear vector con los resultados
  c(cantidad, descripcion, p_unit, importe)
})



# Crear el data frame
df <- as.data.frame(do.call(rbind, datos_separados), stringsAsFactors = FALSE)
colnames(df) <- c("Cantidad", "Descripcion", "P.Unit", "Importe")
print(df[2])
# Imprimir el data frame






