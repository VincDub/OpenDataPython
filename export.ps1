
$dir = Get-Location 
$dir = [regex]::Escape($dir)
$commande = "library(knitr);library(rmarkdown);setwd('$dir');rmarkdown::render('memoire.Rmd','pdf_document')"
Rscript.exe -e $commande