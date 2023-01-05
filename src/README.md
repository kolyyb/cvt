# PROJET CV ONLINE THIERRY ARONOFF
## Développement d'un CV en ligne  
  
  *Backend : Django*  
  **Front   : React**  
  **Hebergement : @home ? Heroku ?**  

### MODELS  

  **Infos**  
      name (CharField)  
      fristname (CharField)  
      email (EmailField)  
      phone (CharField)  
      City (CharField)  
      links (URLField)  

  * Profile  
      intro (TextField)  
  
  * Skills  
      categories (CharField)  
      list (TextField)  

  * Formations  
      name (CharField)  
      centre (CharField)  
      date (DateField)  

  * Missions  
      client (CharField)  
      title (CharField)  
      date (DateField)  
      role (CharField)  
      project (TextField)  
      stack (TextField)  
      

### FONCTIONALITES  

    * Envoi de mails  
        Le recruteur doit pouvoir te contacter via un formulaire de contact   
    * Récuperation CV  
      Le recruteur doit pouvoir téléclacher ton CV au format PDF sécurisé  
