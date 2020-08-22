download mockoon and run it at port 3001.
click on Environment Settings (cog/gear on top right). ensure CORS is enabled.
create /products and paste the following.

/products
```
{
   "products":[
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":1,
         "images":[
            2,
            3
         ],
         "logo":1,
         "name":"Product 1",
         "updated_at":"2020-08-22T08:12:08"
      },
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":2,
         "images":[
            2,
            3
         ],
         "logo":1,
         "name":"Product 2",
         "updated_at":"2020-08-22T08:12:08"
      },
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":1,
         "images":[
            2,
            3
         ],
         "logo":1,
         "name":"Product 3",
         "updated_at":"2020-08-22T08:12:08"
      },
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":3,
         "images":[
            2,
            3
         ],
         "logo":1,
          "name":"Product 4",
         "updated_at":"2020-08-22T08:12:08"
      },
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":4,
         "images":[
            2,
            3
         ],
         "logo":1,
         "name":"Product 5",
         "updated_at":"2020-08-22T08:12:08"
      },
      {
         "created_at":"2020-08-22T08:12:08",
         "description":"new description",
         "id":5,
         "images":[
            2,
            3
         ],
         "logo":1,
         "name":"Product 6",
         "updated_at":"2020-08-22T08:12:08"
      }
   ]
}
```

/products/1
{
  "product": {
    "created_at": "2020-08-22T08:12:08",
    "description": "new description",
    "id": 1,
    "images": [
      2,
      3
    ],
    "logo": 1,
    "name": "Product 1",
    "updated_at": "2020-08-22T08:12:08"
  }
}