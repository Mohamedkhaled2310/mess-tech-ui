'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { mockProducts } from '@/services/mockData';
import { formatPrice } from '@/lib/utils';
import { Plus, Search, Edit3, Trash2, Check, AlertCircle } from 'lucide-react';

export default function AdminProductsPage() {
  const { locale } = useLanguage();
  const [products, setProducts] = useState(mockProducts);
  const [search, setSearch] = useState('');

  const filtered = products.filter(
    (p) =>
      p.name.ar.includes(search) ||
      p.model.toLowerCase().includes(search.toLowerCase()) ||
      p.brand.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div>
            <h1 className="text-2xl font-black text-petrol-900">إدارة المنتجات والمخزون</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              متابعة الأسعار والكميات وتحديث المواصفات الفنية
            </p>
          </div>

          <Link
            href="/admin/products/new"
            className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs shadow-xs"
          >
            <Plus className="w-4 h-4" />
            <span>إضافة منتج جديد</span>
          </Link>
        </div>

        {/* Search */}
        <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-subtle flex items-center justify-between gap-4">
          <div className="relative w-full sm:w-80">
            <Search className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="بحث بالاسم أو الموديل أو الماركة..."
              className="w-full ps-9 pe-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
            />
          </div>

          <span className="text-xs text-slate-500 font-mono">
            إجمالي المنتجات: {filtered.length}
          </span>
        </div>

        {/* Products Table */}
        <div className="bg-white rounded-2xl border border-slate-200 shadow-subtle overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-xs">
              <thead className="bg-slate-50 border-b border-slate-200 text-slate-600 font-bold">
                <tr>
                  <th className="p-3.5 text-start">المنتج</th>
                  <th className="p-3.5 text-start">الموديل والماركة</th>
                  <th className="p-3.5 text-start">السعر (ج.م)</th>
                  <th className="p-3.5 text-start">المخزون</th>
                  <th className="p-3.5 text-start">الحالة</th>
                  <th className="p-3.5 text-end">إجراءات</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filtered.map((prod) => (
                  <tr key={prod.id} className="hover:bg-slate-50/70 transition-colors">
                    <td className="p-3.5">
                      <div className="flex items-center gap-3">
                        <img src={prod.image} alt="" className="w-10 h-10 object-contain shrink-0" />
                        <span className="font-bold text-petrol-900 line-clamp-1 max-w-xs">
                          {prod.name.ar}
                        </span>
                      </div>
                    </td>
                    <td className="p-3.5 font-mono">
                      <span className="font-bold text-petrol-700 block">{prod.brand}</span>
                      <span className="text-slate-400 text-[11px]">{prod.model}</span>
                    </td>
                    <td className="p-3.5 font-mono font-black text-petrol-950">
                      {formatPrice(prod.price, locale)}
                    </td>
                    <td className="p-3.5 font-mono font-bold">
                      {prod.stockCount} قطعة
                    </td>
                    <td className="p-3.5">
                      <span className="inline-flex items-center gap-1 text-emerald-600 font-bold text-[11px]">
                        <Check className="w-3.5 h-3.5" />
                        <span>نشط بالموقع</span>
                      </span>
                    </td>
                    <td className="p-3.5 text-end">
                      <div className="flex items-center justify-end gap-2">
                        <Link
                          href={`/product/${prod.id}`}
                          className="p-1.5 rounded-lg text-slate-500 hover:text-petrol-700 hover:bg-petrol-50"
                          title="معاينة"
                        >
                          <Edit3 className="w-3.5 h-3.5" />
                        </Link>
                        <button
                          onClick={() => {
                            if (confirm(`حذف المنتج ${prod.model}؟`)) {
                              setProducts(products.filter((p) => p.id !== prod.id));
                            }
                          }}
                          className="p-1.5 rounded-lg text-rose-500 hover:bg-rose-50"
                          title="حذف"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}
