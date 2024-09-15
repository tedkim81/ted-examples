from openai import OpenAI
client = OpenAI()

response = client.moderations.create(
    input='Hello world!!'
)
print(response)

"""
[응답]

ModerationCreateResponse(
  id='modr-9eZnbPoGwFZvMFFLsh2FElKCMkG1S',
  model='text-moderation-007', 
  results=[
    Moderation(
      categories=Categories(
        harassment=False, 
        harassment_threatening=False, 
        hate=False, 
        hate_threatening=False, 
        self_harm=False, 
        self_harm_instructions=False, 
        self_harm_intent=False, 
        sexual=False, 
        sexual_minors=False, 
        violence=False, 
        violence_graphic=False, 
        self-harm=False, 
        sexual/minors=False, 
        hate/threatening=False, 
        violence/graphic=False, 
        self-harm/intent=False, 
        self-harm/instructions=False, 
        harassment/threatening=False
      ), 
      category_scores=CategoryScores(
        harassment=0.00024542518076486886, 
        harassment_threatening=1.7658060187386582e-06, 
        hate=0.0001562936813570559, 
        hate_threatening=1.5562417132741757e-08, 
        self_harm=6.0528477661137e-06, 
        self_harm_instructions=3.418466349103255e-06, 
        self_harm_intent=5.13201484864112e-06, 
        sexual=8.383840031456202e-05, 
        sexual_minors=1.0267183824907988e-05, 
        violence=8.173494279617444e-05, 
        violence_graphic=3.2687780731066596e-06, 
        self-harm=6.0528477661137e-06, 
        sexual/minors=1.0267183824907988e-05, 
        hate/threatening=1.5562417132741757e-08, 
        violence/graphic=3.2687780731066596e-06, 
        self-harm/intent=5.13201484864112e-06, 
        self-harm/instructions=3.418466349103255e-06, 
        harassment/threatening=1.7658060187386582e-06
      ), 
      flagged=False
    )
  ]
)
"""