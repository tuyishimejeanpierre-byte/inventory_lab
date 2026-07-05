## project structure
Route	Input	Output	Changes Data	CLI Trigger
GET /inventory	None	All products	No	View Inventory
GET /inventory/<id>	Product ID	One product	No	View Product
POST /inventory	Product details	Created product	Yes	Add Product
PATCH /inventory/<id>	Product ID + updates	Updated product	Yes	Update Product
DELETE /inventory/<id>	Product ID	Success message	Yes	Delete Product
GET /search	Product name/barcode	Open Food Facts result	No	Find Item on API