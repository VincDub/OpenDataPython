
$dir = Get-Location 
$dir = [regex]::Escape($dir)
$commande = "library(knitr);library(rmarkdown);setwd('$dir');rmarkdown::render('test.Rmd','pdf_document')"
Rscript.exe -e $commande