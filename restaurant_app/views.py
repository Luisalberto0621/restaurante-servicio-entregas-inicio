from django.shortcuts import render

def home(request):
    # Lista de productos estáticos
    productos = [
        {'id': 1, 'nombre': 'Pizza Especial', 'precio': 12.99, 'emoji': '🍕', 'descripcion': 'Deliciosa pizza con ingredientes premium y queso mozzarella', 'badge': '🔥 Más vendido', 'rating': 4.8, 'tiempo': '20-25 min'},
        {'id': 2, 'nombre': 'Hamburguesa Gourmet', 'precio': 9.99, 'emoji': '🍔', 'descripcion': 'Carne angus con queso cheddar y vegetales frescos', 'badge': '⭐ Nuevo', 'rating': 4.6, 'tiempo': '15-20 min'},
        {'id': 3, 'nombre': 'Ensalada César', 'precio': 7.99, 'emoji': '🥗', 'descripcion': 'Lechuga romana, crutones, parmesano y aderezo césar', 'badge': '', 'rating': 4.4, 'tiempo': '10-15 min'},
        {'id': 4, 'nombre': 'Pasta Carbonara', 'precio': 11.99, 'emoji': '🍝', 'descripcion': 'Pasta con salsa cremosa, panceta y queso parmesano', 'badge': '💫 Especial', 'rating': 4.7, 'tiempo': '18-22 min'},
        {'id': 5, 'nombre': 'Sushi Mixto', 'precio': 15.99, 'emoji': '🍣', 'descripcion': 'Variedad de sushi con salmón, atún y aguacate', 'badge': '🔥 Más vendido', 'rating': 4.9, 'tiempo': '25-30 min'},
        {'id': 6, 'nombre': 'Tacos al Pastor', 'precio': 8.99, 'emoji': '🌮', 'descripcion': 'Tacos con carne adobada, piña y cebolla', 'badge': '', 'rating': 4.5, 'tiempo': '12-15 min'},
        {'id': 7, 'nombre': 'Lasagna', 'precio': 10.99, 'emoji': '🍝', 'descripcion': 'Capas de pasta, carne, salsa de tomate y queso', 'badge': '', 'rating': 4.6, 'tiempo': '22-25 min'},
        {'id': 8, 'nombre': 'Helado Artesanal', 'precio': 5.99, 'emoji': '🍨', 'descripcion': 'Helado cremoso con sabores a elección', 'badge': '⭐ Nuevo', 'rating': 4.8, 'tiempo': '5-8 min'},
    ]
    return render(request, 'restaurant_app/home.html', {'productos': productos})