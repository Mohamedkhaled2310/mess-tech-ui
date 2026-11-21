'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { ArrowRight, ArrowLeft, Check, Plus, Trash2, UploadCloud } from 'lucide-react';

export default function AdminAddProductPage() {
  const router = useRouter();
  const { dir } = useLanguage();

  const [nameAr, setNameAr] = useState('');
  const [nameEn, setNameEn] = useState('');
  const [brand, setBrand] = useState('Cisco');
  const [model, setModel] = useState('');
  const [category, setCategory] = useState('switches');
  const [price, setPrice] = useState('');
  const [oldPrice, setOldPrice] = useState('');
  const [stock, setStock] = useState('10');
  const [briefAr, setBriefAr] = useState('');

  const [specs, setSpecs] = useState([
    { keyAr: 'عدد المنافذ', keyEn: 'Ports', valAr: '24 منفذ Gigabit PoE+', valEn: '24x GbE PoE+' },
  ]);

  const addSpecRow = () => {
    setSpecs([...specs, { keyAr: '', keyEn: '', valAr: '', valEn: '' }]);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    alert('تم حفظ المنتج بنجاح وإضافته للكتالوج!');
    router.push('/admin/products');
  };

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-200 pb-5">
          <div className="flex items-center gap-3">
            <Link
              href="/admin/products"
              className="p-2 rounded-xl border border-slate-200 hover:bg-slate-100 text-slate-700"
            >
              {dir === 'rtl' ? <ArrowRight className="w-4 h-4" /> : <ArrowLeft className="w-4 h-4" />}
            </Link>
            <div>
              <h1 className="text-xl sm:text-2xl font-black text-petrol-900">إضافة منتج شبكات جديد</h1>
              <p className="text-xs text-slate-500">إدخال المواصفات والأسعار والموديل لقاعدة البيانات</p>
            </div>
          </div>
        </div>

        {/* Form */}
        <form onSubmit={handleSave} className="max-w-4xl space-y-6">
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-5">
            <h3 className="font-extrabold text-sm text-petrol-900 border-b border-slate-100 pb-3">
              1. البيانات الأساسية والموديل
            </h3>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">اسم المنتج بالعربية *</label>
                <input
                  type="text"
                  required
                  value={nameAr}
                  onChange={(e) => setNameAr(e.target.value)}
                  placeholder="سويتش سيسكو كاتاليست 24 بورت..."
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Product Name (English) *</label>
                <input
                  type="text"
                  required
                  value={nameEn}
                  onChange={(e) => setNameEn(e.target.value)}
                  placeholder="Cisco Catalyst 24-Port Switch..."
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">العلامة التجارية (Brand) *</label>
                <select
                  value={brand}
                  onChange={(e) => setBrand(e.target.value)}
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 font-bold focus:outline-none focus:ring-2 focus:ring-petrol-500"
                >
                  <option value="Cisco">Cisco Systems</option>
                  <option value="MikroTik">MikroTik RouterBOARD</option>
                  <option value="Ubiquiti">Ubiquiti UniFi</option>
                  <option value="Synology">Synology NAS</option>
                  <option value="Huawei">Huawei eKit</option>
                  <option value="APC">APC Schneider</option>
                  <option value="Grandstream">Grandstream</option>
                  <option value="D-Link">D-Link</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">كود الموديل الدقيق (Model Code) *</label>
                <input
                  type="text"
                  required
                  value={model}
                  onChange={(e) => setModel(e.target.value)}
                  placeholder="C1000-24P-4G-L"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">القسم والتصنيف *</label>
                <select
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 font-bold focus:outline-none focus:ring-2 focus:ring-petrol-500"
                >
                  <option value="switches">سويتشات Switches</option>
                  <option value="wifi">حلول الواي فاي WiFi</option>
                  <option value="storage">تخزين شبكي NAS</option>
                  <option value="ups">مزودات طاقة UPS</option>
                  <option value="attendance">أجهزة البصمة</option>
                  <option value="screens">شاشات تفاعلية</option>
                  <option value="voip">سنترالات وهواتف VoIP</option>
                  <option value="passive">كابلات وبنية تحتية</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">الكمية بالمخزون *</label>
                <input
                  type="number"
                  required
                  value={stock}
                  onChange={(e) => setStock(e.target.value)}
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 font-mono focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>
            </div>

            {/* Pricing */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">سعر البيع (ج.م) *</label>
                <input
                  type="number"
                  required
                  value={price}
                  onChange={(e) => setPrice(e.target.value)}
                  placeholder="18480"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 font-mono font-bold focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">السعر قبل الخصم (اختياري)</label>
                <input
                  type="number"
                  value={oldPrice}
                  onChange={(e) => setOldPrice(e.target.value)}
                  placeholder="22176"
                  className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-200 font-mono focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>
            </div>
          </div>

          {/* Submit */}
          <div className="flex items-center gap-3">
            <button
              type="submit"
              className="px-6 py-3 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-extrabold text-xs flex items-center gap-2 shadow-sm transition-all"
            >
              <Check className="w-4 h-4" />
              <span>حفظ ونشر المنتج</span>
            </button>
            <Link
              href="/admin/products"
              className="px-5 py-3 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 font-bold text-xs"
            >
              إلغاء
            </Link>
          </div>
        </form>
      </main>
    </div>
  );
}
