package state.artigo;

public class EstadoAprovado implements Estado {
	
	private Artigo artigo;
	
	public EstadoAprovado(Artigo artigo) {
		this.artigo = artigo;
	}

		
	@Override
	public void publicar() {
		// faz nada
		
	}

	@Override
	public void reprovar() {
		
		// faz nada
	}
	
	

}
