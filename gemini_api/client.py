from google import genai

def get_movie_resume (title, genre, release_date ):
    prompt = f"Faça um resumo do filme, {title} {genre} {release_date}, com no máximo 300 caracteres. Não precisa relevar nada muito a fundo da trama, somente pro leitor se conceituar da história."
    client = genai.Client(api_key = 'AIzaSyBV3Kh5u3YLvMlnqhJUe8M6kXAGSn8gaII')
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = [prompt]
    )
    return response.text