import React, { useState, useEffect } from "react";
import axios from "axios";
import { List, Avatar, Skeleton, Button } from 'antd';
import { Link } from "react-router-dom";

const Products = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [products, setProducts] = useState([]);

  useEffect(
    () => {
      axios.get('http://localhost:5001/products').then((res) => {
        setProducts(res.data.products);
        setIsLoading(false);
      })
    },
    []
  );

  return (
    <>
      <Button type="primary"><Link to="products/new">New Product</Link></Button>

      <List
        itemLayout="vertical"
        size="large"
        pagination={{
          onChange: page => {
            console.log(page);
          },
          pageSize: 5,
        }}
        dataSource={products}
        renderItem={item => (
          <List.Item
            key={item.title}
          >
            <Skeleton loading={isLoading}>
              <List.Item.Meta
                avatar={<Avatar shape="square" size="large" src="https://via.placeholder.com/150" />}
                title={<Link to={`/products/${item.id}`}>{item.name}</Link>}
                description={item.description}
              />
              {item.content}
            </Skeleton>
          </List.Item>
        )}
      />
    </>
  )
}

export default Products