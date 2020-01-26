(define (problem Bicicletas-b)
  (:domain Bicicletas-a)  
  (:objects  
  joao
  jose
  maria 

  BicicletarioCAIS
  BicicletarioALFANDEGA
  BicicletarioSANTA
  BicicletarioMERCADO
  BicicletarioDIARIO
  BicicletarioREPUBLICA

  localCAIS
  localALFANDEGA
  localMERCADO
  localDIARIO
  localREPUBLICA
  
)

  (:init  
  (pedalavel BicicletarioCAIS BicicletarioALFANDEGA)
  (pedalavel BicicletarioALFANDEGA BicicletarioCAIS)

  (pedalavel BicicletarioCAIS BicicletarioREPUBLICA)
  (pedalavel BicicletarioREPUBLICA BicicletarioCAIS)

  (pedalavel BicicletarioALFANDEGA BicicletarioSANTA)
  (pedalavel BicicletarioSANTA BicicletarioALFANDEGA)

  (pedalavel BicicletarioSANTA BicicletarioDIARIO) 
  (pedalavel BicicletarioDIARIO BicicletarioSANTA)

  (pedalavel BicicletarioSANTA BicicletarioMERCADO)
  (pedalavel BicicletarioMERCADO BicicletarioSANTA)

  (pedalavel BicicletarioMERCADO BicicletarioDIARIO)
  (pedalavel BicicletarioDIARIO BicicletarioMERCADO)

  (pedalavel BicicletarioDIARIO BicicletarioREPUBLICA)
  (pedalavel BicicletarioREPUBLICA BicicletarioDIARIO)

  (caminhavel BicicletarioREPUBLICA localREPUBLICA)
  (caminhavel localREPUBLICA BicicletarioREPUBLICA)

  (caminhavel BicicletarioALFANDEGA localALFANDEGA)
  (caminhavel localALFANDEGA BicicletarioALFANDEGA)

  (caminhavel BicicletarioCAIS localCAIS)
  (caminhavel localCAIS BicicletarioCAIS)

  (caminhavel BicicletarioDIARIO localDIARIO)
  (caminhavel localDIARIO BicicletarioDIARIO)

  (caminhavel BicicletarioMERCADO localMERCADO)
  (caminhavel localMERCADO BicicletarioMERCADO)
  
  (at joao BicicletarioDIARIO)
  (at jose BicicletarioCAIS)
  (at maria BicicletarioALFANDEGA)
 
  (visitavel joao localDIARIO)
  (visitavel jose localCAIS)
  (visitavel maria localALFANDEGA)

  )
  
 (:goal (and(and(and(and(and (visitavel joao localCAIS )(visitavel maria localDIARIO) )(at maria localMERCADO))(at joao localALFANDEGA))(visitavel jose localREPUBLICA))(at jose localMERCADO) )
 
)
)
  