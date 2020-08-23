import React, { useState, useEffect } from "react";
import axios from "axios";
import { Spin, Descriptions, List, Avatar, Skeleton, Button } from 'antd';
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

const Product = (props) => {
  const [isLoading, setIsLoading] = useState(true);
  const [product, setProduct] = useState([]);
  let { id } = useParams();

  useEffect(
    () => {
      axios.get(`http://localhost:5001/products/${id}`).then((res) => {
        setProduct(res.data);
        setIsLoading(false);
      })
    },
    []
  );

  return (
    isLoading ? <Spin /> :
      <>
        <img width='50%' shape="square" size="large" src={`http://localhost:5001${product.logo.url}`} />
        <Descriptions title="Product Info" layout="vertical">
          <Descriptions.Item label="Name">{product.name}</Descriptions.Item>
          <Descriptions.Item label="Description">{product.description}</Descriptions.Item>
        </Descriptions>
        <Button type="primary"><Link to={`/products/${id}/product_variants/new`}>New Product Variant</Link></Button>

        <List
          itemLayout="vertical"
          size="large"
          pagination={{
            onChange: page => {
              console.log(page);
            },
            pageSize: 5,
          }}

          dataSource={product.variants}
          renderItem={item => (
            <List.Item
              key={item.name}
            >
              <Skeleton loading={isLoading}>
                <List.Item.Meta
                  title={<Link to={`/products/${item.id}`}>{item.name}</Link>}
                />

                {
                  item.images.map((image) => {
                  return (
                    <img key={image.name} height="200" src={`http://localhost:5001${image.url}`} />
                    )
                  })
                }

              {item.color}-{item.size}
              </Skeleton>
            </List.Item>
          )}
        />
      </>

  )
}

export default Product