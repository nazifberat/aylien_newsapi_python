# Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the entity | [optional] 
**links** | [**EntityLinks**](EntityLinks.md) |  | [optional] 
**stock_tickers** | **list[str]** | The stock tickers of the entity (might be empty) | [optional] 
**types** | **list[str]** | An array of the entity types | [optional] 
**overall_sentiment** | [**EntitySentiment**](EntitySentiment.md) |  | [optional] 
**overall_prominence** | **float** | Describes how relevant an entity is to the article | [optional] 
**overall_frequency** | **int** | Amount of entity surface form mentions in the article | [optional] 
**body** | [**EntityInText**](EntityInText.md) |  | [optional] 
**title** | [**EntityInText**](EntityInText.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


