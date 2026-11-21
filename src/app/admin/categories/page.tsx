'use client';

import React, { useState } from 'react';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { mockCategories } from '@/services/mockData';
import { Layers, Plus, Edit2, Trash2 } from 'lucide-react';

export default function AdminCategoriesPage() {
  const [categories, setCategories] = useState(mockCategories);

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div>
            <h1 className="text-2xl font-black text-petrol-900">إدارة الأقسام والتصنيفات</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              ترتيب أقسام المتجر وبانرات العرض لخطوط الإنتاج المختلفة
            </p>
          </div>

          <button
            onClick={() => alert('إضافة قسم جديد')}
            className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs shadow-xs"
          >
            <Plus className="w-4 h-4" />
            <span>إضافة تصنيف جديد</span>
          </button>
        </div>

        {/* Categories Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {categories.map((cat) => (
            <div
              key={cat.id}
              className="bg-white rounded-2xl border border-slate-200 shadow-subtle overflow-hidden flex flex-col justify-between"
            >
              <div>
                <div className="relative h-36 w-full bg-slate-100 overflow-hidden">
                  <img src={cat.image} alt="" className="w-full h-full object-cover" />
                  <span className="absolute top-2.5 end-2.5 px-2 py-0.5 rounded-full bg-white/90 text-petrol-900 font-mono font-bold text-[11px] shadow-xs">
                    {cat.count} جهاز
                  </span>
                </div>

                <div className="p-4 space-y-1">
                  <h3 className="font-extrabold text-sm text-petrol-900">{cat.title.ar}</h3>
                  <span className="text-[11px] font-mono text-sky-700 block">{cat.title.en}</span>
                  <p className="text-xs text-slate-500 line-clamp-2 leading-relaxed pt-1">
                    {cat.desc.ar}
                  </p>
                </div>
              </div>

              <div className="p-4 pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                <button className="text-sky-700 font-bold hover:underline flex items-center gap-1">
                  <Edit2 className="w-3.5 h-3.5" />
                  <span>تعديل البانر</span>
                </button>
                <button
                  onClick={() => {
                    if (confirm(`حذف قسم ${cat.title.ar}؟`)) {
                      setCategories(categories.filter((c) => c.id !== cat.id));
                    }
                  }}
                  className="text-rose-600 font-bold hover:underline flex items-center gap-1"
                >
                  <Trash2 className="w-3.5 h-3.5" />
                  <span>حذف</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
