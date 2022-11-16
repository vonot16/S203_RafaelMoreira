package br.inatel.labs.labads.padraomvc.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class OlaMundoController {
	
	@GetMapping("/ola")
	public String getOla(Model model) {
		
		model.addAttribute("usuario", "Leticia");
		
		return "ola-mundo";
		//String proximaView = "ola-mundo";
		//return proximaView; 
	}

}
